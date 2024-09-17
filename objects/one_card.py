from objects.game import *
from objects.compare import *
import math

# MERGE FROM HERE
def get_valid_tricks(cards: list[Card], trick_to_beat: list[Card]) -> list[list[Card]]:
    cards = Hand.sort_by_strength(cards)
    valid_tricks = []

    for card in cards:
        trick = [card]
        if is_trick_stronger(trick, trick_to_beat):
            valid_tricks.append(trick)

    return valid_tricks

def calculate_aggression(remaining_cards: int) -> float:
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

def calculate_trick_strength(cards: list[Card], remaining_deck: list[Card]) -> float:
    num_beaten = sum(1 for c in remaining_deck if Card.strength(c) > Card.strength(cards[0]))
    probability_of_beaten = num_beaten / len(remaining_deck)

    return probability_of_beaten


def one_card_trick(state: Game) -> list[Card]:
    remaining_deck = state.remaining_deck
    # state.state.toBeat.cards = Hand.to_cards(state.state.toBeat.cards) # NOTE: should be done already 
    trick_to_beat = state.state.toBeat.cards
    valid_tricks = get_valid_tricks(state.hand.cards, trick_to_beat)
    if not valid_tricks: return []

    aggression = calculate_aggression(len(remaining_deck))
    trick_probabilities = [calculate_trick_strength(trick, remaining_deck) for trick in valid_tricks]
    print(valid_tricks)
    print(trick_probabilities)
    if (aggression > 0.6):
        return valid_tricks[-1]
    else:
        for i, trick in enumerate(valid_tricks):
            # in a full deck, TS can be beaten by 30% of the cards
            # i.e., if the card is stronger than TS, and aggression is low then save the card for later
            if trick_probabilities[i] > 0.7: 
                return trick
            
    return []



