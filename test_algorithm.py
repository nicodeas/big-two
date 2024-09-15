from algorithm import *
from mock import players, matchHistory

class TestCard:
    def test_greater_than(self):
        a = Card("2S")
        b = Card("2H")
        c = Card("2S")
        d = Card("KS")

        assert a > b
        # strictly greater than
        assert not a > c
        assert not d > a

    def test_less_than(self):
        a = Card("2S")
        b = Card("2H")
        c = Card("2S")
        d = Card("KS")

        assert b < a
        # strictly less than
        assert not c < a
        assert not a < d

    def test_equality(self):
        a = Card("2S")
        b = Card("2S")
        assert a == b


class TestHand:
    def test_get_2_card_tricks(self):
        a = Card("2D")
        b = Card("2C")
        c = Card("2H")
        d = Card("2S")
        # (2D,2C), (2D,2H), (2D,2S), (2C,2H), (2C,2S), (2H,2S)
        expected = [(a, b), (a, c), (a, d), (b, c), (b, d), (c, d)]
        two_card_tricks, _ = Hand.get_2_card_tricks([a, b, c, d])
        assert two_card_tricks == expected

    def test_get_3_card_tricks(self):
        a = Card("2D")
        b = Card("2C")
        c = Card("2H")
        d = Card("2S")
        # (2D,2C), (2D,2H), (2D,2S), (2C,2H), (2C,2S), (2H,2S)
        expected = [(a, b, c), (a, b, d), (a, c, d), (b, c, d)]
        three_card_tricks, _ = Hand.get_3_card_tricks([a, b, c, d])
        assert three_card_tricks == expected

    def test_action_outputs_strings(self):
        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=['KH', '3H'],  # Example hand
            toBeat=None,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData=''  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert all(isinstance(card, str) for card in action)
    
    def test_start_of_game(self):
        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=['KH', 'AH', '2S', '5C', '5S', '6C', '6S', '7D', '7C', 'TS', 'JS', 'QC', '3D'],  # Example hand
            toBeat=None,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData=''  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ['3D']

    def test_first_move_1_card_trick(self):
        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=['3H', '4H', '5S', '6C'],
            toBeat=None,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData=''  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ['3H']

    def test_first_move_2_card_trick(self):
        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=['2S', '4H', '4S', '3C'],
            toBeat=None,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData=''  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ['4H', '4S']
    
    def test_first_move_3_card_trick(self):
        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=['3S', '4H', '4S', '4C'],
            toBeat=None,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData=''  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ['4C', '4H', '4S']

    def test_1_card_trick_strength(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=['QS'] # Example cards played in the trick
        )

        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=['3C', '3H', '3S', '5C', '5S', '6C', '6S', '7D', '7C', 'TS', 'JS', 'QC', 'KH'],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData=''  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ['KH']

    def test_2_card_trick_strength(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=['5D', '5H'] # Example cards played in the trick
        )

        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=['3C', '3H', '3S', '5C', '5S', '6C', '6S', '7D', '7C', 'TS', 'JS', 'QC', 'KH'],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData=''  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ['5C', '5S']

    def test_3_card_trick_strength(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=['5D', '5H', '5S'] # Example cards played in the trick
        )

        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=['3C', '3H', '3S', '5C', '7S', '6C', '6S', '7D', '7C', 'TS', 'JS', 'QC', 'KH'],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData=''  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ['7D', '7C', '7S']



class TestGameHistory:
    def test_updating_cards(self):
        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=players,  # Empty list for players
            myHand=['KD', '3H', '5C', '5S', '6C', '6S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
            toBeat=None,  # No need to define, set as None
            matchHistory=matchHistory,  # Empty match history
            myData=''  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        card_data = json.loads(myData)['remaining_deck']
        assert len(card_data) == 37