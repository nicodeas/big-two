from objects.hand import *

# MERGE FROM HERE
class Game:
    def __init__(self, state):
        # reset the game state with the data object
        self.deck = self.generate_deck()
        self.hand = Hand(state.myHand)

    @staticmethod
    def generate_deck():
        deck = set()
        for r in Rank.ranks:
            for s in Suit.suits:
                deck.add(r+s)
        return deck

        # remove ur cards from the deck and each move keep track of which cards are left
    def updateDeck():
        pass

    def __str__():
        # convert this to a data object we can send and receive back for each game
        pass