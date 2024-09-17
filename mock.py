from typing import List
from classes import *
from objects.game import Game

deck = list(Game.generate_deck())

# Mock data for Trick objects
trick1 = Trick(playerNum=0, cards=["3D"])
trick2 = Trick(playerNum=1, cards=["4S"])
trick3 = Trick(playerNum=2, cards=["KH"])
trick4 = Trick(playerNum=3, cards=[])
trick5 = Trick(playerNum=0, cards=['2S'])
trick6 = Trick(playerNum=1, cards=[])
trick7 = Trick(playerNum=2, cards=[])
trick8 = Trick(playerNum=3, cards=[])

# Mock data for GameHistory (1 round with 3 tricks)
round1 = [trick1, trick2, trick3, trick4, trick5, trick6, trick7, trick8]
# round1 = [trick1]
gameHistory = GameHistory(finished=False, winnerPlayerNum=0, gameHistory=[round1])

# Mock data for Player objects
player0 = Player(points=0, handSize=11)
player1 = Player(points=0, handSize=12)
player2 = Player(points=0, handSize=12)
player3 = Player(points=0, handSize=13)

# Mocking MatchState object
matchHistory = [gameHistory]
players = [player0, player1, player2, player3]

mock_trick = Trick(
    playerNum=1,  # Mock player number, for example player 1
    cards=deck[-2:] # Example cards played in the trick
)

# Mock object creation with only myHand being relevant
mock_match_state = MatchState(
    myPlayerNum=1,  # You can mock this as 0
    players=players,  # Empty list for players
    # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
    myHand=['3C', '2D', '2C', '2H', '2S'],  # Example hand
    toBeat=None,  # No need to define, set as None
    matchHistory=matchHistory,  # Empty match history
    # myData="",
    myData='{"remaining_deck": ["QD", "2H", "4C", "7H", "JC", "KS", "2D", "JD", "4D", "2C", "8S", "9S", "KC", "6H", "QH", "5H", "3C", "3S", "AC", "AD", "AH", "TH", "AS", "TD", "8D", "TC", "8C", "8H", "6D", "7S", "9H", "QS", "5D", "9C", "JH", "4H", "9D"]}'  # Empty string for myData
)

# # Now, you can access the myHand attribute of the mock object
# print(mock_match_state.myHand)
# print(mock_trick.cards)
