from typing import List
from classes import *
from objects.game import Game

deck = list(Game.generate_deck())

mock_trick = Trick(
    playerNum=1,  # Mock player number, for example player 1
    cards=[] # Example cards played in the trick
)

# Mock object creation with only myHand being relevant
mock_match_state = MatchState(
    myPlayerNum=0,  # You can mock this as 0
    players=[],  # Empty list for players
    myHand=deck[:5],  # Example hand
    toBeat=mock_trick,  # No need to define, set as None
    matchHistory=[],  # Empty match history
    myData=''  # Empty string for myData
)

# # Now, you can access the myHand attribute of the mock object
# print(mock_match_state.myHand)
# print(mock_trick.cards)
