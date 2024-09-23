from objects.game import *
from objects.compare import *
import math

# MERGE FROM HERE
def get_all_valid_tricks_one(cards: list[Card]) -> list[list[Card]]:
    tricks = [[c] for c in Hand.sort_by_strength(cards)]
    valid_tricks = []

    for trick in tricks:
            valid_tricks.append(trick)

    return valid_tricks

def get_valid_tricks_one(cards: list[Card], trick_to_beat: list[Card]) -> list[list[Card]]:
    tricks = [[c] for c in Hand.sort_by_strength(cards)]
    valid_tricks = []

    for trick in tricks:
        if is_trick_stronger(trick, trick_to_beat):
            valid_tricks.append(trick)

    return valid_tricks

def calculate_aggression_one(remaining_cards: int) -> float:
    # Parameters
    max_cards = 39  # Starting number of cards (52 - 13) start of game
    min_cards = 4   # Lowest number of cards (1 for each player)
    
    # Normalize the number of remaining cards to a range from 0 to 1
    normalized_cards = (max_cards - remaining_cards) / (max_cards - min_cards)
    # Parameters for the sigmoid function
    scaling_factor = 0.05  # Scaling factor to control the growth
    growth_rate = 6.0  # Rate of growth
    
    # Calculate sigmoid function
    aggression = min(scaling_factor * (math.exp(growth_rate * normalized_cards) - 1), 1)
    
    return aggression

def calculate_trick_strength_one(trick: list[Card], possible_tricks: list[list[Card]]) -> float:
    num_beaten = sum(1 for opponent_trick in possible_tricks if is_trick_stronger(opponent_trick, trick))
    probability_of_beaten = num_beaten / len(possible_tricks)

    return probability_of_beaten

def valuate(trick: list[Card], remaining_deck: list[Card]) -> float:
    value = 1       # start off with a valuation of unity

    remaining_valuations = map(Card.strength, remaining_deck)
    # penalise high cards
    for card in trick:
        strength = Card.strength(card)
        if strength < max(remaining_valuations):            # TODO: maybe bias depending on how many cards remaining can beat it
            value *= 1 - strength / 51

    # penalise cards that form combinations
    for card in trick:
        for valid_trick in (*get_all_valid_tricks_two(),*get_all_valid_tricks_three(),*get_all_valid_tricks_five()):
            if card in valid_trick:
                value *= 0.5

    return value


def one_card_trick(state: Game) -> list[Card]:
    remaining_deck: list[Card] = list(state.remaining_deck)
    
    if (state.state.toBeat and len(state.state.toBeat.cards) > 0):
        trick_to_beat = state.state.toBeat.cards
        valid_tricks = get_valid_tricks_one(state.hand.cards, trick_to_beat)
    else:
        valid_tricks = get_all_valid_tricks_one(state.hand.cards)
    
    if not valid_tricks: 
        print("No valid tricks")
        return []

    # Add algorithm below
    aggression = calculate_aggression_one(len(remaining_deck))
    print(f"Aggression value is: {aggression} for {len(remaining_deck)} num of cards")
    possible_tricks = [[card] for card in remaining_deck]
    trick_probabilities = [calculate_trick_strength_one(trick, possible_tricks) for trick in valid_tricks]
    print(valid_tricks)
    print(trick_probabilities)

    if (aggression > 0.9):
            # if game is near end game then play your strongest card
        for i, trick in enumerate(valid_tricks):
            # if game is getting closer to end game then play a strong card
            if trick_probabilities[i] <= 0.2: 
                return trick
            
        return valid_tricks[-1]

    if (aggression > 0.7):
        for i, trick in enumerate(valid_tricks):
            # if game is getting closer to end game then play a strong card
            if trick_probabilities[i] <= 0.35: 
                return trick
            
    if (aggression > 0.25):
        # To give cards priority
        for i, trick in enumerate(valid_tricks):
            # if in mid game the card can be beaten by a large portion of cards, discard it
            if trick_probabilities[i] > 0.7: 
                return trick
            
            # Else, play a stronger than average card
            if 0.2 <= trick_probabilities[i] <= 0.4: 
                return trick
        
        # if neither then just play the lowest valid trick
        return valid_tricks[0]
            
        
            
    for i, trick in enumerate(valid_tricks):
        # if the card can be beaten by 40% of the cards during early game
        if trick_probabilities[i] >= 0.4: 
            return trick
            
    return []



