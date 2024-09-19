from classes import *
from itertools import combinations
import json
import math

from objects.imports import *

def cards_to_strings(func):
    def wrapper(*args, **kwargs):
        action, myData = func(*args, **kwargs)
        action = [str(card) for card in action]
        myData = str(myData)
        # print(f"send data: {len(json.loads(myData)['remaining_deck'])}")
        return action, myData
    return wrapper

class Algorithm:
    def __init__(self):
        self.game = None
        self.state = None

    def start_of_game(self):
        # TODO: have start of game with 5 card trick
        
        tricks, _ = Hand.get_3_card_tricks(self.game.hand.cards)
        for trick in tricks:
            if Card('3D') in trick:
                return [*trick], self.game
            
        tricks, _ = Hand.get_2_card_tricks(self.game.hand.cards)
        for trick in tricks:
            if Card('3D') in trick:
                return [*trick], self.game
        
        return [Card('3D')], self.game
    
    def first_move(self):
        if Card('3D') in self.game.hand:
            return self.start_of_game()
        trick_sizes = [5, 3, 2, 1]
        for trick_size in trick_sizes:
            action, myData = self.play_a_move(trick_size)
            if action:
                return action, myData
            
        # Can't pass so play lowest valid card
        tricks = [[c] for c in Hand.sort_by_strength(self.game.hand)]
        return tricks[0], myData
    
    def one_card_trick(self):
        trick = one_card_trick(self.game)
        return trick, self.game

    def two_card_trick(self):
        trick = two_card_trick(self.game)
        return trick, self.game

    def three_card_trick(self):
        trick = three_card_trick(self.game)
        return trick, self.game

    def five_card_trick(self):
        trick = five_card_trick(self.game)
        return trick, self.game

    def tempPassMove(self):
        return [], self.game
    
    def play_a_move(self, trick_size: int):
        if trick_size == 1:
            action, myData = self.one_card_trick()
        elif trick_size == 2:
            action, myData = self.two_card_trick()
        elif trick_size == 3:
            action, myData = self.three_card_trick()
        else:
            action, myData = self.five_card_trick()

        return action, myData

    
    @cards_to_strings
    def getAction(self, state: MatchState):
        action = []  # The cards you are playing for this trick
        if not state.myData: state.myData = "{}"
        state.myData = json.loads(state.myData)
        if 'remaining_deck' in state.myData:
            print(f"recv data: {len(state.myData['remaining_deck'])}")

        if (state.toBeat and len(state.toBeat.cards) > 0): 
            state.toBeat.cards = Hand.to_cards(state.toBeat.cards)
        
        # NOTE: Modify state as needed before this

        myData = state.myData  # Communications from the previous iteration
        self.state = state
        self.game = Game(self.state)
        self.game.update_remaining_deck()

        print(f"Cards remaining: {self.game}")
        print(f"My hand:  {Hand.sort_by_strength(self.game.hand.cards)}")

        if (not state.toBeat or len(state.toBeat.cards) == 0): 
            return self.first_move()
        
        
        trick_size = len(state.toBeat.cards)
        action, myData = self.play_a_move(trick_size)
        
        # TODO Write your algorithm logic here

        return action, myData
    

