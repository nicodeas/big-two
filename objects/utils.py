from objects.card import *
from objects.hand import *

# MERGE FROM HERE
def is_trick_contained(trick1: list[Card], trick2: list[Card]):
    for card in trick1:
        if card not in trick2:
            return False
        
    return True


