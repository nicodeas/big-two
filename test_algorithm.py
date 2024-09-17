from out.algorithm import *
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
            cards=['JS'] # Example cards played in the trick
        )

        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=['TS', 'JD', 'JC', 'KH'],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData='{"remaining_deck": ["QD", "2S", "4C", "7H", "JC"]}'  # Empty string for myData
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


class TestAlgorithmOneCard:
    def test_passing_early_game(self):
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
            myData='{"remaining_deck": ["QD", "JH", "2S", "7H", "JC", "KS", "2D", "JD", "4D", "2C", "8S", "9S", "KC", "6H", "QH", "5H", "3C", "3S", "AC", "AD", "TH", "AS", "TD", "8D", "TC", "8C", "8H", "6D", "7S", "9H"]}'  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == []

    def test_no_aggression(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=['4D'] # Example cards played in the trick
        )
                
        mock_match_state = MatchState(
            myPlayerNum=1,  # You can mock this as 0
            players=players,  # Empty list for players
            # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
            myHand=['3C', '4C', '5C', '6H', '2H'],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=matchHistory,  # Empty match history
            myData='{"remaining_deck": ["QD", "JH", "2S", "7H", "JC", "KS", "2D", "JD", "4D", "2C", "8S", "9S", "KC", "6H", "QH", "5H", "3C", "3S", "AC", "AD", "TH", "AS", "TD", "8D", "TC", "8C", "8H", "6D", "7S", "9H"]}'  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ['4C']
    
    def test_medium_aggression(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=['QD'] # Example cards played in the trick
        )
                
        mock_match_state = MatchState(
            myPlayerNum=1,  # You can mock this as 0
            players=players,  # Empty list for players
            # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
            myHand=['QS', '2S', '9S', 'KC', '7C', 'KD', 'AS', 'AH', 'QH', '4S', '7H', 'TD', '2H'],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=matchHistory,  # Empty match history
            myData='{"remaining_deck": ["JS", "9D", "7S", "8H", "KS", "8S", "AD", "8C", "4C", "AC", "5S", "9C", "KH", "QC", "5D", "4D", "8D", "6D", "9H", "5C", "2C", "5H", "3S", "TH", "4H", "2D", "3H", "TS", "TC"]}'  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ['QH']

    def test_high_aggression(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=['JD'] # Example cards played in the trick
        )

        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=['TS', 'JD', 'JS', 'KH'],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData='{"remaining_deck": ["QD", "2S", "4C", "7H", "JC"]}'  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ['KH']

class TestAlgorithmTwoCard:
    def test_passing_early_game(self):
        mock_trick = Trick(
        playerNum=1,  # Mock player number, for example player 1
        cards=['4D', '4S'] # Example cards played in the trick
        )
                
        mock_match_state = MatchState(
            myPlayerNum=1,  # You can mock this as 0
            players=players,  # Empty list for players
            # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
            myHand=['3C', '4C', '5C', '2D', '2H'],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=matchHistory,  # Empty match history
            myData='{"remaining_deck": ["QD", "JH", "2S", "7H", "JC", "KS", "2D", "JD", "4D", "2C", "8S", "9S", "KC", "6H", "QH", "5H", "3C", "3S", "AC", "AD", "TH", "AS", "TD", "8D", "TC", "8C", "8H", "6D", "7S", "9H"]}'  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == []