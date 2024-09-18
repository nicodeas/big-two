from objects.game import *
from objects.compare import *
import math

# MERGE FROM HERE
def get_all_valid_tricks_five(cards: list[Card]) -> list[list[Card]]:
    tricks_dict, _ = Hand.get_5_card_tricks(cards)
    valid_tricks = []

    for trick_type, trick_tuple in tricks_dict.items():
        trick_list, _ = trick_tuple
        for trick in trick_list:
                valid_tricks.append(trick)

    return valid_tricks

def get_valid_tricks_five(cards: list[Card], trick_to_beat: list[Card]) -> list[list[Card]]:
    tricks_dict, _ = Hand.get_5_card_tricks(cards)
    trick_to_beat_type = Hand.get_5_card_trick_type(trick_to_beat)
    valid_tricks = []

    for trick_type, trick_tuple in tricks_dict.items():
        trick_list, _ = trick_tuple
        if trick_type == trick_to_beat_type:
            for trick in trick_list:
                if is_trick_stronger(trick, trick_to_beat):
                    valid_tricks.append(trick)
        elif trick_type > trick_to_beat_type:
            for trick  in trick_list:
                valid_tricks.append(trick)

    return valid_tricks

def five_card_trick(state: Game) -> list[Card]:
    remaining_deck: list[Card] = list(state.remaining_deck)

    if (state.state.toBeat and len(state.state.toBeat.cards) > 0):
        trick_to_beat = state.state.toBeat.cards
        valid_tricks = get_valid_tricks_five(state.hand.cards, trick_to_beat)
    else:
        valid_tricks = get_all_valid_tricks_five(state.hand.cards)

    if not valid_tricks: 
        print("No valid tricks")
        return []
    
    return valid_tricks[-1]
    
    return []



