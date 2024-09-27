from objects.hand import *
from objects._classes import *
import json

# MERGE FROM HERE
class Game:
    def __init__(self, state: MatchState):
        # reset the game state with the data object
        self.hand = Hand(state.myHand)
        self.state = state
        self.decode()
        
        self.rounds_played = state.matchHistory[-1].gameHistory if state.matchHistory  else []
        # self.round = len(self.rounds_played)-1
        self.opponents = [x.handSize for x in state.players]
        del self.opponents[self.state.myPlayerNum]

    @staticmethod
    def generate_deck():
        deck = set()
        for r in Rank.ranks:
            for s in Suit.suits:
                deck.add(Card(r+s))
        return deck
    
    def generate_deck_from_data(self):
        card_data = self.state.myData['remaining_deck']
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

    def encode(self):
        myData = {}
        myData['remaining_deck'] = [str(card) for card in self.remaining_deck]
        return myData

    def decode(self):
        if 'remaining_deck' in self.state.myData:
            self.remaining_deck = self.generate_deck_from_data()
        else:
            self.remaining_deck = self.generate_deck()
            [self.remove_card(card) for card in self.hand]
            

    def __repr__(self):
        # convert this to a data object we can send and receive back for each game
        myData = self.encode()
        json_data = json.dumps(myData)
        return json_data
    