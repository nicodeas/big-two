from classes import *

from objects.imports import *

# from mock import mock_match_state

class Algorithm:

    def tempPassMove(self):
        return [], ""

    def getAction(self, state: MatchState):
        action = []  # The cards you are playing for this trick
        myData = state.myData  # Communications from the previous iteration
        
        game = Game(state)
        game.hand.cards = [Card(c) for c in state.myHand]
        # print(game.hand.cards)
        # return self.tempPassMove()
        game.hand.cards = Hand.sort_by_strength(game.hand.cards)
        print(game.hand.cards)
        cardsToBeat = state.toBeat.cards
        
        if (len(cardsToBeat) > 1): return self.tempPassMove()
        if (len(cardsToBeat) == 0):
            return [str(game.hand.cards[0])], ""

        cardToBeat = Card(cardsToBeat[0])
        # print("Card to beat: " + str(cardToBeat))
        cardStrength = Card.strength(cardToBeat)

        for card in game.hand.cards:
            if (Card.strength(card) > cardStrength):
                return [str(card)], ""
        
        # TODO Write your algorithm logic here

        return action, myData
    

# algo = Algorithm()
# action, myData = algo.getAction(state=mock_match_state)

# print(action)
# print(myData)