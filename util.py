import random


class Deck:
    cards: list[str]

    def __init__(self) -> None:
        suits = ["D", "C", "H", "S"]
        ranks = ["3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A", "2"]
        self.cards = [r + s for s in suits for r in ranks]

    def shuffle_deck(self) -> None:
        random.shuffle(self.cards)
