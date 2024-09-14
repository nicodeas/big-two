# MERGE FROM HERE
class Suit:
    D = "D"
    C = "C"
    H = "H"
    S = "S"

    suits = [D, C, H, S]

    @staticmethod
    def strength(suit):
        strength = {Suit.D: 1, Suit.C: 2, Suit.H: 3, Suit.S: 4}
        return strength[suit]