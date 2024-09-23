from algorithm import *
from mock import mock_match_state, matchHistory, players

mock_trick = Trick(
    playerNum=1,  # Mock player number, for example player 1
    cards=['3S'],  # Example cards played in the trick
)

mock_match_state = MatchState(
    myPlayerNum=1,  # You can mock this as 0
    players=players,  # Empty list for players
    # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
    myHand=['4S', '6D', '8C', 'QS', 'KS', '2C'],  # Example hand
    toBeat=mock_trick,  # No need to define, set as None
    matchHistory=None,  # Empty match history
    myData='{"remaining_deck": ["JC", "TC", "KC", "QD", "KD", "TS", "2S", "9S", "9H", "AD", "5D", "7S", "7C", "2D"]}',  # Empty string for myData
)
algo = Algorithm()
action, myData = algo.getAction(state=mock_match_state)
print(action)
# assert action == []