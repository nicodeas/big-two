from classes import *

from objects.imports import *

def cards_to_strings(func):
    def wrapper(*args, **kwargs):
        action, myData = func(*args, **kwargs)
        action = [str(card) for card in action]
        return action, myData
    return wrapper

class Algorithm:
    def __init__(self):
        self.game = None
        self.state = None

    def start_of_game(self):
        tricks, _ = Hand.get_2_card_tricks(self.game.hand.cards)
        for trick in tricks:
            if Card('3D') in trick:
                return [*trick], ""
        
        return [Card('3D')], ""
    
    def first_move(self):
        if Card('3D') in self.game.hand:
            return self.start_of_game()
        
        tricks, _ = Hand.get_2_card_tricks(self.game.hand.cards)
        print(tricks)
        if (len(tricks)) > 0:
            return [*tricks[0]], ""
        
        self.game.hand.cards = Hand.sort_by_strength(self.game.hand)
        print(f"Sorted deck (first move): {self.game.hand.cards}")
        return [self.game.hand.cards[0]], ""
    
    def one_card_trick(self):
        tricks = Hand.sort_by_strength(self.game.hand)
        trick_to_beat = self.state.toBeat.cards
        
        print(f"Sorted deck (one card trick): {tricks}")
        for trick in tricks:
            if (is_trick_stronger([trick], trick_to_beat)):
                return [trick], ""
        
        return self.tempPassMove()

    def two_card_trick(self):
        tricks, _ = Hand.get_2_card_tricks(self.game.hand.cards)
        trick_to_beat = self.state.toBeat.cards

        print(f"Two card tricks): {tricks}")
        for trick in tricks:
            if (is_trick_stronger(trick, trick_to_beat)):
                return [*trick], ""


        return self.tempPassMove()

    def three_card_trick(self):
        return self.tempPassMove()

    def five_card_trick(self):
        return self.tempPassMove()

    def tempPassMove(self):
        return [], ""
    
    @cards_to_strings
    def getAction(self, state: MatchState):
        action = []  # The cards you are playing for this trick
        myData = state.myData  # Communications from the previous iteration
        self.game = Game(state)
        self.state = state

        if (not state.toBeat or len(state.toBeat.cards) == 0): 
            return self.first_move()

        self.state.toBeat.cards = [Card(c) for c in self.state.toBeat.cards]
        num_of_cards = len(state.toBeat.cards)

        if num_of_cards == 1:
            return self.one_card_trick()
        elif num_of_cards == 2:
            return self.two_card_trick()
        elif num_of_cards == 3:
            return self.three_card_trick()
        else:
            return self.five_card_trick()
        
        # TODO Write your algorithm logic here

        return action, myData
    

