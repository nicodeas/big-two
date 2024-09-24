from objects.game import *
from objects.compare import *

# MERGE FROM HERE
class Valuator:
    @staticmethod
    def valuate(trick: list[Card], cards: list[Card], remaining_deck: list[Card]) -> float:
        value = 1       # start off with a valuation of unity

        remaining_valuations = map(Card.strength, remaining_deck)
        # penalise high cards
        for card in trick:
            strength = Card.strength(card)
            if strength < max(remaining_valuations):            # TODO: maybe bias depending on how many cards remaining can beat it
                value *= 1 - strength / 51

        # penalise cards that form combinations
        for card in trick:
            for valid_trick in (*get_all_valid_tricks_two(cards),*get_all_valid_tricks_three(cards),*get_all_valid_tricks_five(cards)):
                if card in valid_trick:
                    value *= 0.5

        return value
