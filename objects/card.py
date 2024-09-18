from objects.rank import *
from objects.suit import *


# MERGE FROM HERE
class Card:
    rank: str
    suit: str
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

    @staticmethod
    def strength(card):
        assert isinstance(card, Card)
        return (Rank.strength(card.rank) - 1) * 4 + Suit.strength(card.suit) - 1

    def suit_strength(card):
        assert isinstance(card, Card)
        return (Rank.strength(card.rank)) - 1 + (Suit.strength(card.suit) - 1) * 13

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

    def __hash__(self) -> int:
        return hash(f"{self.rank}{self.suit}")

    def __repr__(self) -> str:
        return f"{self.rank}{self.suit}"

    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"

