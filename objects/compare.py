from objects.card import *

# MERGE FROM HERE
def is_one_card_trick_stronger(trick1, trick2):
    return Card.strength(trick1[0]) > Card.strength(trick2[0])

def is_two_card_trick_stronger(trick1, trick2):
    trick1_strength = max(Card.strength(trick1[0]), Card.strength(trick1[1]))
    trick2_strength = max(Card.strength(trick2[0]), Card.strength(trick2[1]))
    
    return trick1_strength > trick2_strength

def is_trick_stronger(trick1, trick2):
    size = len(trick2)
    if size == 1:
        return is_one_card_trick_stronger(trick1, trick2)
    elif size == 2:
        return is_two_card_trick_stronger(trick1, trick2)

    return False

def get_trick_value(trick):
    pass
