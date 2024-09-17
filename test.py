from algorithm import *
from mock import mock_match_state, matchHistory, players

mock_trick = Trick(
    playerNum=1,  # Mock player number, for example player 1
    cards=['AH'] # Example cards played in the trick
)
        
mock_match_state = MatchState(
    myPlayerNum=1,  # You can mock this as 0
    players=players,  # Empty list for players
    # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
    myHand=['3C', '4C', '5C', '6H', '2H'],  # Example hand
    toBeat=mock_trick,  # No need to define, set as None
    matchHistory=matchHistory,  # Empty match history
    myData='{"remaining_deck": ["QD", "2S", "4C", "7H", "JC", "KS", "2D", "JD", "4D", "2C", "8S", "9S", "KC", "6H", "QH", "5H", "3C", "3S", "AC", "AD", "TH", "AS", "TD", "8D", "TC", "8C", "8H", "6D", "7S", "9H"]}'  # Empty string for myData
)
algo = Algorithm()
action, myData = algo.getAction(state=mock_match_state)
print(action)

# from objects.imports import *
# if __name__ == "__main__":
#     one_card_trick(algo.game)