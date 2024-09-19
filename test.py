from algorithm import *
from mock import mock_match_state, matchHistory, players

mock_trick = Trick(
    playerNum=1,  # Mock player number, for example player 1
    cards=[],  # Example cards played in the trick
)

mock_match_state = MatchState(
    myPlayerNum=1,  # You can mock this as 0
    players=players,  # Empty list for players
    # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
    myHand=['9S', '9H', '9D', 'KD', 'KC'],  # Example hand
    toBeat=None,  # No need to define, set as None
    matchHistory=matchHistory,  # Empty match history
    myData='{"remaining_deck": ["TC", "6H", "3S", "7S", "9C", "QS"]}',  # Empty string for myData
)
algo = Algorithm()
action, myData = algo.getAction(state=mock_match_state)
print(action)
# assert action == []

