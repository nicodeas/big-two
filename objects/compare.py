from objects.card import *
from objects.hand import *

# MERGE FROM HERE
def is_one_card_trick_stronger(trick1: list[Card], trick2: list[Card]):
    return Card.strength(trick1[0]) > Card.strength(trick2[0])

def is_two_card_trick_stronger(trick1: list[Card], trick2: list[Card]):
    trick1_strength = max(Card.strength(trick1[0]), Card.strength(trick1[1]))
    trick2_strength = max(Card.strength(trick2[0]), Card.strength(trick2[1]))
    
    return trick1_strength > trick2_strength

def is_three_card_trick_stronger(trick1: list[Card], trick2: list[Card]):
    return trick1[0] > trick2[0]

def is_five_card_trick_stronger(trick1: list[Card], trick2: list[Card]):
    trick1_type = Hand.get_5_card_trick_type(trick2)
    trick2_type = Hand.get_5_card_trick_type(trick2)

    if trick2_type > trick1_type:
        return False
    
    if (trick2_type == 0): return is_straight_stronger(trick1, trick2)
    if (trick2_type == 1): return is_flush_stronger(trick1, trick2)
    if (trick2_type == 2): return is_full_house_stronger(trick1, trick2)
    if (trick2_type == 3): return is_four_of_a_kind_stronger(trick1, trick2)
    if (trick2_type == 4): return is_straight_flush_stronger(trick1, trick2)
    
def is_straight_stronger(trick1: list[Card], trick2: list[Card]):
    trick1 = Hand.sort_by_strength(trick1)
    trick2 = Hand.sort_by_strength(trick2)
    return Card.strength(trick1[-1]) > Card.strength(trick2[-1])

def is_flush_stronger(trick1: list[Card], trick2: list[Card]):
    trick1 = Hand.sort_by_strength(trick1)
    trick2 = Hand.sort_by_strength(trick2)
    for i in range(4, -1, -1):
        if Rank.strength(trick1[i].rank) > Rank.strength(trick2[i].rank):
            return True
        elif Rank.strength(trick1[i].rank) < Rank.strength(trick2[i].rank):
            return False
        
    return Suit.strength(trick1[-1].suit) > Suit.strength(trick2[-1].suit)


def is_full_house_stronger(trick1: list[Card], trick2: list[Card]):
    trick1 = Hand.sort_by_strength(trick1)
    trick2 = Hand.sort_by_strength(trick2)
    # Compare the middle card rank as this is guaranteed to be the triple
    return Card.strength(trick1[2]) > Card.strength(trick2[2])

def is_four_of_a_kind_stronger(trick1: list[Card], trick2: list[Card]):
    trick1 = Hand.sort_by_strength(trick1)
    trick2 = Hand.sort_by_strength(trick2)
    # Compare the second card rank as this is guaranteed to be the four of a kind
    return Card.strength(trick1[1]) > Card.strength(trick2[1])

def is_straight_flush_stronger(trick1: list[Card], trick2: list[Card]):
    trick1 = Hand.sort_by_strength(trick1)
    trick2 = Hand.sort_by_strength(trick2)
    if Card.strength(trick1[-1]) == Card.strength(trick2[-1]):
        return Rank.strength(trick1[-1].suit) > Rank.strength(trick2[-1].suit)
    else:
        return Card.strength(trick1[-1]) > Card.strength(trick2[-1])



def is_trick_stronger(trick1: list[Card], trick2: list[Card]):
    size = len(trick2)
    if size == 1:
        return is_one_card_trick_stronger(trick1, trick2)
    elif size == 2:
        return is_two_card_trick_stronger(trick1, trick2)
    elif size == 3:
        return is_three_card_trick_stronger(trick1, trick2)
    else:
        return is_five_card_trick_stronger(trick1, trick2)

    return False

def get_trick_value(trick):
    pass
