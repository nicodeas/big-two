from objects.hand import *
from objects._classes import *
import json

# MERGE FROM HERE
class Game:
    def __init__(self, state: MatchState):
        # reset the game state with the data object
        self.hand = Hand(state.myHand)
        if not state.myData:
            self.remaining_deck = self.generate_deck()
            [self.remove_card(card) for card in self.hand]
        else:
            self.remaining_deck = self.generate_deck_from_data(state.myData)
        self.rounds_played = state.matchHistory[-1].gameHistory if state.matchHistory  else []
        # self.round = len(self.rounds_played)-1

    @staticmethod
    def generate_deck():
        deck = set()
        for r in Rank.ranks:
            for s in Suit.suits:
                deck.add(Card(r+s))
        return deck
    
    @staticmethod
    def generate_deck_from_data(json_data):
        card_data = json.loads(json_data)
        deck = set()
        for card in card_data:
            deck.add(Card(card))
        return deck

        # remove ur cards from the deck and each move keep track of which cards are left
    def update_remaining_deck(self):
        # maybe keep track of the last round only and keep state updated by myData
        for rounds in self.rounds_played:
            for tricks in rounds:
                for card in tricks.cards:
                    self.remove_card(card)

    def remove_card(self, card):
        self.remaining_deck.discard(Card(str(card)))

    def __repr__(self):
        # convert this to a data object we can send and receive back for each game
        json_data = json.dumps([str(card) for card in self.remaining_deck])
        return json_data
    