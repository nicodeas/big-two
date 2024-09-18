from itertools import combinations
from objects.card import *


# MERGE FROM HERE
class Hand:
    cards: list[Card] = None
    TWO_CARD_STRENGTH_MULTIPLIER = 2
    THREE_CARD_STRENGTH_MULTIPLIER = 4
    STRAIGHT_STRENGTH_MULTIPLIER = 8

    # TODO: figure out multiplier
    FOUR_OF_A_KIND_MULTIPLIER = 1

    def __init__(self, cards: list[Card] | list[str]) -> None:
        self.cards = self.to_cards(cards)

    @staticmethod
    def sort_by_suit(cards: list[Card]) -> list[Card]:
        return sorted(cards, key=lambda x: Suit.strength(x.suit))

    @staticmethod
    def sort_by_rank(cards: list[Card]) -> list[Card]:
        return sorted(cards, key=lambda x: Rank.strength(x.rank))

    @staticmethod
    def sort_by_strength(cards: list[Card]) -> list[Card]:
        return sorted(cards, key=lambda x: Card.strength(x))

    @staticmethod
    def sort_by_suit_strength(cards: list[Card]) -> list[Card]:
        return sorted(cards, key=lambda x: Card.suit_strength(x))

    @staticmethod
    def to_cards(cards: list[Card] | list[str]) -> list[Card]:
        return [Card(str(c)) for c in cards]

    def get_hand(self) -> list[Card]:
        return self.cards

    def get_hand_strength(self):
        pass

    @staticmethod
    def get_2_card_tricks(cards: list[Card]) -> tuple[list[tuple[Card, Card]], int]:
        cards.sort(key=lambda x: Card.strength(x))
        # TODO: maybe this has a tools that simplify this
        # https://docs.python.org/3/library/itertools.html#itertools
        tricks: list[tuple[Card, Card]] = []
        value = 0

        # Generate all 3-card combinations
        for combo in combinations(cards, 2):
            if combo[0].rank == combo[1].rank:
                tricks.append(combo)
                value += sum(Card.strength(card) for card in combo)

        return tricks, value * Hand.TWO_CARD_STRENGTH_MULTIPLIER

    @staticmethod
    def get_3_card_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card]], int]:
        # count numer of cards per rank
        # if 3 cards -> 1 combination
        # 4 cards -> 4C3 combinations = 4 (if 4 cards, u have a four of a kind)
        # https://docs.python.org/3/library/itertools.html#itertools.combinations
        cards.sort(key=lambda x: Card.strength(x))
        tricks: list[tuple[Card, Card, Card]] = []
        value = 0

        # Generate all 3-card combinations
        for combo in combinations(cards, 3):
            if combo[0].rank == combo[1].rank == combo[2].rank:
                tricks.append(combo)
                value += sum(Card.strength(card) for card in combo)

        return tricks, value * Hand.THREE_CARD_STRENGTH_MULTIPLIER

    @staticmethod
    def get_straight_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # TODO: easy
        cards.sort(key=lambda x: Card.strength(x))
        tricks: list[tuple[Card, Card, Card]] = []
        value = 0

        l = 0
        cur_trick = []
        while (l < len(cards)):
            card = cards[l]
            if not cur_trick:
                cur_trick.append(card)
            else:
                if Rank.strength(card.rank) == Rank.strength(cur_trick[-1].rank):
                    l+=1
                    continue
            
            if Rank.strength(card.rank) == Rank.strength(cur_trick[-1].rank) + 1:
                cur_trick.append(card)
            else:
                cur_trick = [card]

            if len(cur_trick) == 5:
                is_not_straight_flush = False

                for i in range(1, len(cur_trick)):
                    if not cur_trick[i].suit == cur_trick[i-1].suit:
                        is_not_straight_flush = True
                        break
                
                if is_not_straight_flush:
                    tricks.append(tuple(cur_trick))
                    value += sum(
                    Card.strength(card)
                        for card in cur_trick
                    )

                cur_trick = cur_trick[1:]
            l+=1
        
        return tricks, value


    @staticmethod
    def get_flush_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # TODO: easy
        pass

    @staticmethod
    def get_full_house_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # many combinations
        pass

    @staticmethod
    def get_four_of_a_kind_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        cards.sort(key=lambda x: Card.strength(x))
        tricks: list[tuple[Card, Card, Card]] = []
        value = 0
        # init sliding window of len 4
        for i in range(len(cards) - 3):
            if cards[i].rank == cards[i + 3].rank:
                # TODO: idk if this is the fastest way to do it, are we required to copy each time?
                four_of_a_kind_trick = cards[i : i + 4].copy()
                # add the kicker
                for j in range(len(cards)):
                    if j < i or j >= i + 4:
                        four_of_a_kind_trick.append(cards[j])
                        four_of_a_kind_trick_and_extra = tuple(four_of_a_kind_trick)
                        tricks.append(four_of_a_kind_trick_and_extra)
                        # remove extra card
                        four_of_a_kind_trick.pop()
                        value += sum(
                            Card.strength(card)
                            for card in four_of_a_kind_trick_and_extra
                        )
        return tricks, value * 1

    @staticmethod
    def get_straight_flush_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # get straight trick + check that all same suit
        pass

    @staticmethod
    def get_5_card_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # maybe return as a dictionary with keys 1, 2, 3, 4, 5 for relative strength of 5 card tricks
        # might make it easier to compare against

        # TODO: weakest(top) to strongest (bottom)
        # get_straight_tricks
        # get_flush_tricks
        # get_full_house_tricks
        # get_four_of_a_kind_tricks
        # get_straight_flush_tricks

        tricks = {
            0: Hand.get_straight_tricks(cards),
            1: Hand.get_flush_tricks(cards),
            2: Hand.get_full_house_tricks(cards),
            3: Hand.get_four_of_a_kind_tricks(cards),
            4: Hand.get_straight_flush_tricks(cards),
        }

    @staticmethod
    def get_5_card_trick_type(
        cards: list[Card],
    ) -> int:
        # returnw which type of 5 card trick it is: 0-4
        pass

    def __iter__(self) -> list[Card]:
        return iter(self.cards)

