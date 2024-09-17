from objects.game import *

def one_card_trick(state) -> list[Card]:
    cards = Hand.sort_by_strength(state.hand)
    print([Card.strength(card) for card in cards])
    print([Card.suit_strength(card) for card in cards])
    
    return []