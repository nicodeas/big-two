from classes import *


class Suit:
    D = "D"
    C = "C"
    H = "H"
    S = "S"

    @staticmethod
    def strength(suit):
        strength = {Suit.D: 1, Suit.C: 2, Suit.H: 3, Suit.S: 4}
        return strength[suit]


class Rank:
    _3 = "3"
    _4 = "4"
    _5 = "5"
    _6 = "6"
    _7 = "7"
    _8 = "8"
    _9 = "9"
    T = "T"
    J = "J"
    Q = "Q"
    K = "K"
    A = "A"
    _2 = "2"

    @staticmethod
    def strength(rank):
        strength = {
            Rank._3: 1,
            Rank._4: 2,
            Rank._5: 3,
            Rank._6: 4,
            Rank._7: 5,
            Rank._8: 6,
            Rank._9: 7,
            Rank.T: 8,
            Rank.J: 9,
            Rank.Q: 10,
            Rank.K: 11,
            Rank.A: 12,
            Rank._2: 13,
        }
        # 2x as rank more important than suite
        return 2 * strength[rank]


class Card:
    rank: Rank
    suit: Suit
    rank_mapping = {
        "3": Rank._3,
        "4": Rank._4,
        "5": Rank._5,
        "6": Rank._6,
        "7": Rank._7,
        "8": Rank._8,
        "9": Rank._9,
        "T": Rank.T,
        "J": Rank.J,
        "Q": Rank.Q,
        "K": Rank.K,
        "A": Rank.A,
        "2": Rank._2,
    }
    suit_mapping = {"D": Suit.D, "C": Suit.C, "H": Suit.H, "S": Suit.S}

    def __init__(self, card: str) -> None:
        self.rank = self.rank_mapping[card[0]]
        self.suit = self.suit_mapping[card[1]]

    def strength(card):
        assert isinstance(card, Card)
        return Rank.strength(card.rank) + Suit.strength(card.suit)

    def __eq__(self, other) -> bool:
        assert isinstance(other, Card)
        return self.rank == other.rank and self.suit == other.suit

    def __gt__(self, other) -> bool:
        assert isinstance(other, Card)
        if Rank.strength(self.rank) > Rank.strength(other.rank):
            return True
        elif Rank.strength(self.rank) < Rank.strength(other.rank):
            return False
        elif Suit.strength(self.suit) > Suit.strength(other.suit):
            return True
        return False

    def __lt__(self, other) -> bool:
        assert isinstance(other, Card)
        if Rank.strength(self.rank) < Rank.strength(other.rank):
            return True
        elif Rank.strength(self.rank) > Rank.strength(other.rank):
            return False
        elif Suit.strength(self.suit) < Suit.strength(other.suit):
            return True
        return False


class Hand:
    cards: list[Card] = None
    TWO_CARD_STRENGTH_MULTIPLIER = 2
    THREE_CARD_STRENGTH_MULTIPLIER = 4
    STRAIGH_STRENGTH_MULTIPLIER = 8

    def __init__(self, cards: list[Card]) -> None:
        self.cards = cards

    def sort_by_suit(self) -> None:
        self.cards.sort(key=lambda x: x.suit)

    def sort_by_rank(self) -> None:
        self.cards.sort(key=lambda x: x.rank)

    def get_hand(self) -> list[Card]:
        return self.cards

    def get_hand_strength(self):
        pass

    def get_2_card_tricks(self) -> tuple[list[tuple[Card, Card]], int]:
        self.sort_by_suit()
        self.sort_by_rank()
        tricks: list[tuple[Card, Card]] = []
        value = 0
        for i in range(1, len(self.cards)):
            if self.cards[i].rank == self.cards[i - 1].rank:
                tricks.append((self.cards[i - 1], self.cards[i]))
                value += Card.strength(self.cards[i - 1]) + Card.strength(self.cards[i])
        return tricks, value * self.TWO_CARD_STRENGTH_MULTIPLIER

    def get_3_card_tricks(self) -> tuple[list[tuple[Card, Card, Card]], int]:
        pass

    def get_straight_tricks(
        self,
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # TODO: easy
        pass

    def get_flush_tricks(self) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # TODO: easy
        pass

    def get_full_house_tricks(
        self,
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # many combinations
        pass

    def get_four_of_a_kind_tricks(
        self,
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # how to figure out what card to throw away in this?
        pass

    def get_straight_flush_tricks(
        self,
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # get straight trick + check that all same suit
        pass

    def get_5_card_tricks(
        self,
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # TODO: weakest(top) to strongest (bottom)
        # get_straight_tricks
        # get_flush_tricks
        # get_full_house_tricks
        # get_four_of_a_kind_tricks
        # get_straight_flush_tricks
        pass


class Algorithm:

    def getAction(self, state: MatchState):
        action = []  # The cards you are playing for this trick
        myData = state.myData  # Communications from the previous iteration

        # TODO Write your algorithm logic here

        return action, myData
