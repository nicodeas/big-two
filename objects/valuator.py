from objects.game import *
from objects.compare import *

from objects.two_card import *
from objects.three_card import *
from objects.five_card import *

# MERGE FROM HERE
class Valuator:
    # valuate: takes in list of playable tricks all consisting of n cards (as well as auxiliary data) and evaluates their strength
    @staticmethod
    def valuate(tricks: list[list[Card]], hand: list[Card], remaining_deck: list[Card], aggression: float = 1) -> list[tuple[list[Card], float]]:
        # NOTE/TODO: aggression defaults to 1, which occurs for 5-card tricks.
        # This makes sense since we ideally want to play our best 5-card tricks early to prevent opponents from playing theirs,
        # with the hopes that we can break theirs up before they get a chance to play it.
        # Similar logic also occurs when setting value = 1 for strength >= max(remaining_valuations)
        # This should probably be more obvious in the code logic :/ - feel free to fix
        valuation = []

        for trick in tricks:
            value = 1       # start off with unity value

            # penalise tricks containing cards that are part of larger tricks
            for card in trick:
                if Valuator.in_trick(card, hand, size=len(trick)+1):
                    value *= 0.2

            # penalise high cards ... unless they're the strongest in the remaining deck
            # (save our high cards for when they count)
            remaining_valuations = list(map(Card.strength, remaining_deck))
            for card in trick:
                strength = Card.strength(card)
                if len(remaining_valuations) > 0 and strength < max(remaining_valuations):
                    value *= Valuator.aggression_curve(aggression, strength)
                
                if strength >= max(remaining_valuations):
                    value = 1               # if the card is the strongest in the deck, play it!

            valuation.append( (trick, value) )

        valuation.sort(key=lambda x: x[1], reverse=True)      # sort by highest valuation

        if len(tricks) > 0:
            print(f"[VALUATOR]: valuation of tricks of size {len(tricks[0])} -- {valuation}")

        return valuation

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
        if aggression < 0.25:       # early game -- shed low cards
            return 1 - strength / 51
        elif aggression < 0.75:     # mid game -- play mid-high cards most
            return 1 - ((strength - 36) / 15)**2
        else:                       # late game -- play high cards
            return strength / 51
