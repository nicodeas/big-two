from algorithm import *
from mock import mock_match_state, matchHistory, players
mock_trick = Trick(
    playerNum=1,  # Mock player number, for example player 1
    cards=["QD"],  # Example cards played in the trick
)

mock_match_state = MatchState(
    myPlayerNum=1,  # You can mock this as 0
    players=players,  # Empty list for players
    # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
    myHand=[
        "2S",
        "9S",
        "KC",
        "7C",
        "KD",
        "AS",
        "AH",
        "QH",
        "4S",
        "7H",
        "TD",
        "2H",
    ],  # Example hand
    toBeat=mock_trick,  # No need to define, set as None
    matchHistory=matchHistory,  # Empty match history
    myData='{"remaining_deck": ["JS", "9D", "7S", "8H", "KS", "8S", "AD", "8C", "4C", "AC", "5S", "9C", "KH", "QC", "5D", "4D", "8D", "6D", "9H", "5C", "2C", "5H", "3S", "TH", "4H", "2D", "3H", "TS", "TC"]}',  # Empty string for myData
)
algo = Algorithm()
action, myData = algo.getAction(state=mock_match_state)
# assert action == ["QH"]
# assert action == ["KH"]
print(action)
