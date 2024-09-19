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
    myHand=['9S', 'KD', 'AC'],  # Example hand
    toBeat=mock_trick,  # No need to define, set as None
    matchHistory=matchHistory,  # Empty match history
    myData='{"remaining_deck": ["QS", "6D", "QH", "KS", "9C", "QC", "5D", "5C", "3S", "JD", "6H", "7H", "KH", "8S", "8H", "4S", "5H", "QD", "6C", "9H", "8C", "2D", "7D", "5S", "2S", "JS", "7S", "6S", "8D", "7C", "9D", "3C", "KC", "2C"]}',  # Empty string for myData
)
algo = Algorithm()
action, myData = algo.getAction(state=mock_match_state)
print(action)
# assert action == []

