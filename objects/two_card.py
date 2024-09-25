from objects.game import *
from objects.compare import *
import math

# MERGE FROM HERE
def get_all_valid_tricks_two(cards: list[Card]) -> list[list[Card]]:
    tricks, _ = Hand.get_2_card_tricks(cards)
    valid_tricks = []

    for trick in tricks:
            valid_tricks.append(trick)

    return valid_tricks

def get_valid_tricks_two(cards: list[Card], trick_to_beat: list[Card]) -> list[list[Card]]:
    tricks, _ = Hand.get_2_card_tricks(cards)
    valid_tricks = []

    for trick in tricks:
        if is_trick_stronger(trick, trick_to_beat):
            valid_tricks.append(trick)

    return valid_tricks

def calculate_aggression_two(remaining_cards: int) -> float:
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

def calculate_trick_strength_two(trick: list[Card], possible_tricks: list[list[Card]]) -> float:
    if len(possible_tricks) == 0:
        return 0
    num_beaten = sum(1 for opponent_trick in possible_tricks if is_trick_stronger(opponent_trick, trick))
    probability_of_beaten = num_beaten / len(possible_tricks)

    return probability_of_beaten


def two_card_trick(state: Game) -> list[Card]:
    remaining_deck = list(state.remaining_deck)

    if (state.state.toBeat and len(state.state.toBeat.cards) > 0):
        trick_to_beat = state.state.toBeat.cards
        valid_tricks = get_valid_tricks_two(state.hand.cards, trick_to_beat)
    else:
        valid_tricks = get_all_valid_tricks_two(state.hand.cards)

    if not valid_tricks: 
        print("No valid tricks")
        return []

    # Add algorithm below
    aggression = calculate_aggression_two(len(remaining_deck))
    print(f"Aggression value is: {aggression} for {len(remaining_deck)} num of cards")
    possible_tricks, _ = Hand.get_2_card_tricks(remaining_deck)
    # return []
    trick_probabilities = [calculate_trick_strength_two(trick, possible_tricks) for trick in valid_tricks]
    print(valid_tricks)
    print(trick_probabilities)
    
    valuation = Valuator.valuate(valid_tricks, state.hand.cards, remaining_deck)
    
    if len(valuation) > 0:
        return valuation[0][0]

    return []
