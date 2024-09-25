from objects.game import *
from objects.compare import *

from objects.two_card import *
from objects.three_card import *
from objects.five_card import *

# MERGE FROM HERE
class Valuator:
    # valuate: takes in list of playable tricks all consisting of n cards (as well as auxiliary data) and evaluates their strength
    @staticmethod
    def valuate(tricks: list[list[Card]], hand: list[Card], remaining_deck: list[Card]) -> list[tuple[list[Card], float]]:
        valuation = []

        for trick in tricks:
            value = 1       # start off with unity value

            # penalise tricks containing cards that are part of larger tricks
            for card in trick:
                if Valuator.in_trick(card, hand, size=len(trick)+1):
                    value *= 0.2

            # penalise high cards ... unless they're the strongest in the remaining deck
            # (save our high cards for when they count)
            remaining_valuations = list(map(Card.strength, remaining_deck))
            for card in trick:
                strength = Card.strength(card)
                if len(remaining_valuations) > 0 and strength < max(remaining_valuations):            # TODO: maybe bias depending on how many cards remaining can beat it
                    value *= 1 - strength / 51
                
                if strength >= max(remaining_valuations):
                    value = 1               # if the card is the strongest in the deck, play it!

            valuation.append( (trick, value) )

        valuation.sort(key=lambda x: x[1], reverse=True)      # sort by highest valuation

        if len(tricks) > 0:
            print(f"[VALUATOR]: valuation of tricks of size {len(tricks[0])} -- {valuation}")

        return valuation

    @staticmethod
    def in_trick(card: Card, hand: list[Card], size: int = 2):      # TODO: make hand a class property
        tricks = []

        if size == 2:
            tricks += get_all_valid_tricks_two(hand)
        if size <= 3:
            tricks += get_all_valid_tricks_three(hand)
        if size <= 5:
            tricks += get_all_valid_tricks_five(hand)

        for trick in tricks:
            for c in trick:
                if card == c:
                    return True

        return False
