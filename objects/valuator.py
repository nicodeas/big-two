from objects.game import *
from objects.compare import *
import math

from objects.two_card import *
from objects.three_card import *
from objects.five_card import *

# MERGE FROM HERE

probability_params = {
    1: [],
    2: [],
    3: [],
    5: [],
}


class Valuator:
    @staticmethod
    def hold_back(cards: list[Card], trick_to_beat: list[Card], classifications: any, turns: int, opponents: list[int], trick: list[Card]) -> bool:
        ca = classifications[0]
        cb = classifications[1]
        cc = classifications[2]
        cd = classifications[3]

        if len(trick_to_beat) == 1:
            if len(cards) <= 2: return False
            if any(o < 3 for o in opponents): return False
            if len(ca) < (len(cb) + len(cc) + len(cd)) or min([len(cards), *opponents] > 6):
                if trick == ca[-1]: return True
                return False
        
        elif len(trick_to_beat):
            if len(cards) <= 3: return False
            if all(o > 2 for o in opponents):
                if Rank.strength(trick[0].rank) == Rank.strength(Card('2S').rank): return True
            return False

        elif len(trick_to_beat) == 5:
            # if len(cards) == 5: return False
            # if min([len(cards), *opponents] > 6) and turns <= 4:
            #     if len()
            return False
        return False

    @staticmethod
    def calculate_aggression(remaining_cards: int) -> float:
        # Parameters
        max_cards = 39  # Starting number of cards (52 - 13) start of game
        min_cards = 4   # Lowest number of cards (1 for each player)
        
        # Normalize the number of remaining cards to a range from 0 to 1
        normalized_cards = (max_cards - remaining_cards) / (max_cards - min_cards)
        # Parameters for the sigmoid function
        scaling_factor = 0.05  # Scaling factor to control the growth
        growth_rate = 4.0  # Rate of growth
        
        # Calculate sigmoid function
        aggression = min(scaling_factor * (math.exp(growth_rate * normalized_cards) - 1), 1)
        
        return aggression

    @staticmethod
    def calculate_trick_win_likelihood(trick: list[Card], remaining_deck: list[Card]):
        possible_tricks = []
        if len(trick) == 1:
            possible_tricks = [[card] for card in remaining_deck]
        elif len(trick) == 2:
            possible_tricks, _ = Hand.get_2_card_tricks(remaining_deck)
        elif len(trick) == 3:
            possible_tricks, _ = Hand.get_3_card_tricks(remaining_deck)

        if len(possible_tricks) == 0:
            return 1

        num_beaten = sum(1 for opponent_trick in possible_tricks if is_trick_stronger(opponent_trick, trick))
        probability_of_beaten = num_beaten / len(possible_tricks)

        return 1 - probability_of_beaten    

    @staticmethod
    def discard_trick(tricks: list[list[Card]], hand: list[Card], remaining_deck: list[Card], aggression: float = 1) -> list[Card]:
        tricks.sort(key=lambda x: Valuator.calculate_trick_win_likelihood(x, remaining_deck))
        probabilities = [Valuator.calculate_trick_win_likelihood(trick, remaining_deck) for trick in tricks]
        print(aggression)
        if aggression <= 0.5:
            for i, prob in enumerate(probabilities):
                if prob < 0.9:
                    # use valuator here
                    return tricks[i]
            
            return []
        
        if probabilities[-1] == 1.0:
            # TODO: maybe check for good cards too instead of straight highest but who knows
            return tricks[-1]
        
        return tricks[0]

    @staticmethod
    def reserve_trick_one(tricks: list[list[Card]], hand: list[Card], remaining_deck: list[Card], aggression: float = 1) -> list[Card]:
        # when to play or pass a one card trick
        tricks.sort(key=lambda x: Valuator.calculate_trick_win_likelihood(x, remaining_deck))
        probabilities = [Valuator.calculate_trick_win_likelihood(trick, remaining_deck) for trick in tricks]

        if aggression > 0.7:
            if probabilities[-1] == 1:
                return tricks[-1]
            
        # make this better
        if aggression > 0.5:
            return tricks[0]
        
        return []
            
    @staticmethod
    def reserve_trick(tricks: list[list[Card]], hand: list[Card], remaining_deck: list[Card], aggression: float = 1) -> list[Card]:
        if not tricks:
            return []
        
        if (len(tricks[0]) == 1):
            return Valuator.reserve_trick_one(tricks, hand, remaining_deck, aggression)
        
        # NOTE: Strictly for trick sizes greater than 1

        tricks.sort(key=lambda x: Valuator.calculate_trick_win_likelihood(x, remaining_deck))
        probabilities = [Valuator.calculate_trick_win_likelihood(trick, remaining_deck) for trick in tricks]

        if aggression <= 0.5:
            # use valuator here
            return tricks[0]
        
        for i, prob in enumerate(probabilities):
            if prob > 0.5:
                # use valuator here
                return tricks[i]
        
        return tricks[0]


    # valuate: takes in list of playable tricks all consisting of n cards (as well as auxiliary data) and evaluates their strength
    @staticmethod
    def valuate(tricks: list[list[Card]], hand: list[Card], remaining_deck: list[Card]) -> list[Card]:
        # NOTE/TODO: aggression defaults to 1, which occurs for 5-card tricks.
        # This makes sense since we ideally want to play our best 5-card tricks early to prevent opponents from playing theirs,
        # with the hopes that we can break theirs up before they get a chance to play it.
        # Similar logic also occurs when setting value = 1 for strength >= max(remaining_valuations)
        # This should probably be more obvious in the code logic :/ - feel free to fix
        aggression = Valuator.calculate_aggression(len(remaining_deck))
        valuation = []
        discard = []
        reserve = []

        for trick in tricks:
            reserved = False
            for card in trick:
                if Valuator.in_trick(card, hand, len(trick)+1):
                    reserve.append(trick)
                    reserved = True
                    break

            if not reserved:
                discard.append(trick)

        # NOTE: Create discard and reserve piles
        if len(discard) > 0:
            # choose which trick to discard
            trick = Valuator.discard_trick(discard, hand, remaining_deck, aggression)
            if len(trick) > 0:
                return trick
        
        # choose which trick to play if any at all
        trick = Valuator.reserve_trick(reserve, hand, remaining_deck, aggression)
        return trick

    @staticmethod
    def in_trick(card: Card, hand: list[Card], size: int = 2):      # TODO: make hand a class property
        tricks = []

        if size == 2:
            tricks += get_all_valid_tricks_two(hand)
        if size <= 3:
            tricks += get_all_valid_tricks_three(hand)
        if size <= 5:
            tricks += get_all_valid_tricks_five(hand)

        for trick in tricks:
            for c in trick:
                if card == c:
                    print(f"[VALUATOR]: card {card} in trick {trick}")
                    return True

        return False

    # value certain cards differently at different points in game
    @staticmethod
    def aggression_curve(aggression: float, strength: int) -> float:
        pass
