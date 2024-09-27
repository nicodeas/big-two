from objects.game import *
from objects.compare import *
import math
from objects.valuator import *

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

    trick = Valuator.valuate(valid_tricks, state.hand.cards, remaining_deck)
    return trick
