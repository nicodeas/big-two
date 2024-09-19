import random
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

    @staticmethod
    def random_deck() -> list[Card]:
        deck = [Card(r + s) for s in Suit.suits for r in Rank.ranks]
        random.shuffle(deck)
        return deck

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
        expected = [(a, b, c), (a, b, d), (a, c, d), (b, c, d)]
        three_card_tricks, _ = Hand.get_3_card_tricks([a, b, c, d])
        assert three_card_tricks == expected

    def test_get_four_of_a_kind_tricks(self):
        a = Card("2D")
        b = Card("2C")
        c = Card("2H")
        d = Card("2S")

        # additional unrelated cards
        e = Card("3D")
        f = Card("3C")
        g = Card("TD")
        h = Card("JC")

        hand = [a, b, c, d, e, f, g, h]
        expected = [(a, b, c, d, e), (a, b, c, d, f), (a, b, c, d, g), (a, b, c, d, h)]

        four_of_a_kind_tricks, _ = Hand.get_four_of_a_kind_tricks(hand)
        assert four_of_a_kind_tricks == expected

        # 13 suits, 48 possible additional cards, 13 * 48 = 624
        total_four_of_a_kind_tricks, _ = Hand.get_four_of_a_kind_tricks(
            [Card(r + s) for s in Suit.suits for r in Rank.ranks]
        )
        assert len(total_four_of_a_kind_tricks) == 624

    def test_get_straight(self):
        a = Card("3C")
        b = Card("4C")
        c = Card("5C")
        d = Card("6D")
        e = Card("7D")
        f = Card("7C")
        g = Card("7H")
        h = Card("8D")
        i = Card("TD")
        j = Card("JC")
        k = Card("QS")
        l = Card("KS")
        m = Card("AS")

        myHand=[a, b, c, d, e, f, g, h, i, j, k, l, m]  # Example hand

        expected = [(a, b, c, d, e), (a, b, c, d, f), (a, b, c, d, g), (b, c, d, e, h), (i, j, k, l, m)]
        
        straight_trick, _ = Hand.get_straight_tricks(myHand)
        
        assert straight_trick == expected
    
    def test_get_straight_ignore_flush(self):
        a = Card("3C")
        b = Card("4C")
        c = Card("5C")
        d = Card("6C")
        e = Card("7C")

        myHand=[a, b, c, d, e]  # Example hand
        expected = []
        
        straight_trick, _ = Hand.get_straight_tricks(myHand)
        
        assert straight_trick == expected

    def test_get_straight_flush(self):
        a = Card("3C")
        b = Card("4C")
        c = Card("5C")
        d = Card("6D")
        e = Card("TH")
        f = Card("JD")
        g = Card("QD")
        h = Card("KD")
        i = Card("AD")
        j = Card("2D")

        myHand=[a, b, c, d, e, f, g, h, i, j]  # Example hand

        expected = [(f, g, h, i, j)]
        
        straight_flush_trick, _ = Hand.get_straight_flush_tricks(myHand)
        
        assert straight_flush_trick == expected

        total_straight_flush_tricks, _ = Hand.get_straight_flush_tricks(
            [Card(r + s) for s in Suit.suits for r in Rank.ranks]
        )
        # 23456 is not a valid straight
        assert len(total_straight_flush_tricks) == 36

    def test_get_flush_tricks(self):
        deck = TestHand.random_deck()
        total_flush_tricks, _ = Hand.get_flush_tricks(deck)
        assert len(total_flush_tricks) == 5148

    def test_get_full_house_tricks(self):
        deck = TestHand.random_deck()
        total_full_house_tricks, _ = Hand.get_full_house_tricks(deck)
        assert len(total_full_house_tricks) == 3744

    def test_type_of_trick(self):
        # straight
        hand1 = [Card('3S'), Card('4H'), Card('5D'), Card('6C'), Card('7S')]
        assert Hand.get_5_card_trick_type(hand1) == 0
        
        # flush
        hand2 = [Card('2H'), Card('5H'), Card('7H'), Card('9H'), Card('KH')]
        assert Hand.get_5_card_trick_type(hand2) == 1
        
        # full house
        hand3 = [Card('4S'), Card('4D'), Card('4C'), Card('7H'), Card('7D')]
        assert Hand.get_5_card_trick_type(hand3) == 2
        
        # four of a kind
        hand4 = [Card('9S'), Card('9D'), Card('9H'), Card('9C'), Card('KC')]
        assert Hand.get_5_card_trick_type(hand4) == 3
        
        # straight flush
        hand5 = [Card('3D'), Card('4D'), Card('5D'), Card('6D'), Card('7D')]
        assert Hand.get_5_card_trick_type(hand5) == 4
        
        # straight flush > straight
        hand6 = [Card('5C'), Card('6C'), Card('7C'), Card('8C'), Card('9C')]        
        assert Hand.get_5_card_trick_type(hand6) == 4


    def test_action_outputs_strings(self):
        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=["KH", "3H"],  # Example hand
            toBeat=None,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData="",  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert all(isinstance(card, str) for card in action)

    def test_start_of_game(self):
        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=[
                "KH",
                "AH",
                "2S",
                "5C",
                "5S",
                "6C",
                "6S",
                "7D",
                "7C",
                "TS",
                "JS",
                "QC",
                "3D",
            ],  # Example hand
            toBeat=None,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData="",  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ["3D"]

    def test_first_move_1_card_trick(self):
        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=["3H", "4H", "5S", "6C"],
            toBeat=None,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData="",  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ["3H"]

    def test_first_move_2_card_trick(self):
        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=["2S", "4H", "4S", "3C"],
            toBeat=None,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData="",  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ["4H", "4S"]

    def test_first_move_3_card_trick(self):
        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=["3S", "4H", "4S", "4C"],
            toBeat=None,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData="",  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ["4C", "4H", "4S"]

    def test_1_card_trick_strength(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=["JS"],  # Example cards played in the trick
        )

        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=["TS", "JD", "JC", "KH"],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData='{"remaining_deck": ["QD", "2S", "4C", "7H", "JC"]}',  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ["KH"]

    def test_2_card_trick_strength(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=["5D", "5H"],  # Example cards played in the trick
        )

        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=[
                "3C",
                "3H",
                "3S",
                "5C",
                "5S",
                "6C",
                "6S",
                "7D",
                "7C",
                "TS",
                "JS",
                "QC",
                "KH",
            ],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData="",  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ["5C", "5S"]

    def test_3_card_trick_strength(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=["5D", "5H", "5S"],  # Example cards played in the trick
        )

        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=[
                "3C",
                "3H",
                "3S",
                "5C",
                "7S",
                "6C",
                "6S",
                "7D",
                "7C",
                "TS",
                "JS",
                "QC",
                "KH",
            ],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData="",  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ["7D", "7C", "7S"]

    def test_compare_5_card_tricks(self):
        # straight
        straight1 = [Card('3S'), Card('4H'), Card('5D'), Card('6C'), Card('7S')]
        straight2 = [Card('3S'), Card('4H'), Card('5D'), Card('6C'), Card('7D')]
        assert is_trick_stronger(straight1, straight2) == True
        assert is_trick_stronger(straight2, straight1) == False
        
        # flush
        flush1 = [Card('2H'), Card('5H'), Card('7H'), Card('9H'), Card('KH')]
        flush2 = [Card('2H'), Card('6H'), Card('7H'), Card('9H'), Card('KH')]
        flush3 = [Card('2S'), Card('5S'), Card('7S'), Card('9S'), Card('KS')]

        assert is_trick_stronger(flush1, flush2) == False
        assert is_trick_stronger(flush3, flush1) == True
        
        # full house
        full_house1 = [Card('3H'), Card('3S'), Card('9D'), Card('9C'), Card('9S')]
        full_house2 = [Card('4D'), Card('4C'), Card('4S'), Card('2D'), Card('2C')]
        assert is_trick_stronger(full_house1, full_house2) == True
        assert is_trick_stronger(full_house2, full_house1) == False
        
        # four of a kind
        four_of_a_kind1 = [Card('9S'), Card('9D'), Card('9H'), Card('9C'), Card('KC')]
        four_of_a_kind2 = [Card('8S'), Card('8D'), Card('8H'), Card('8C'), Card('2S')]
        assert is_trick_stronger(four_of_a_kind1, four_of_a_kind2) == True
        assert is_trick_stronger(four_of_a_kind2, four_of_a_kind1) == False
        
        # straight flush
        straight_flush1 = [Card('4S'), Card('5S'), Card('6S'), Card('7S'), Card('8S')]
        straight_flush2 = [Card('3D'), Card('4D'), Card('5D'), Card('6D'), Card('7D')]
        straight_flush3 = [Card('4H'), Card('5H'), Card('6H'), Card('7H'), Card('8H')]
        assert is_trick_stronger(straight_flush1, straight_flush2) == True
        assert is_trick_stronger(straight_flush3, straight_flush1) == False


class TestGameHistory:
    def test_updating_cards(self):
        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=players,  # Empty list for players
            myHand=[
                "KD",
                "3H",
                "5C",
                "5S",
                "6C",
                "6S",
                "7D",
                "7C",
                "TS",
                "JS",
                "QC",
            ],  # Example hand
            toBeat=None,  # No need to define, set as None
            matchHistory=matchHistory,  # Empty match history
            myData="",  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        card_data = json.loads(myData)["remaining_deck"]
        assert len(card_data) == 37


class TestAlgorithmOneCard:
    def test_passing_early_game(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=["AH"],  # Example cards played in the trick
        )

        mock_match_state = MatchState(
            myPlayerNum=1,  # You can mock this as 0
            players=players,  # Empty list for players
            # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
            myHand=["3C", "4C", "5C", "6H", "2H"],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=matchHistory,  # Empty match history
            myData='{"remaining_deck": ["QD", "JH", "2S", "7H", "JC", "KS", "2D", "JD", "4D", "2C", "8S", "9S", "KC", "6H", "QH", "5H", "3C", "3S", "AC", "AD", "TH", "AS", "TD", "8D", "TC", "8C", "8H", "6D", "7S", "9H"]}',  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == []

    def test_no_aggression(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=["4D"],  # Example cards played in the trick
        )

        mock_match_state = MatchState(
            myPlayerNum=1,  # You can mock this as 0
            players=players,  # Empty list for players
            # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
            myHand=["3C", "4C", "5C", "6H", "2H"],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=matchHistory,  # Empty match history
            myData='{"remaining_deck": ["QD", "JH", "2S", "7H", "JC", "KS", "2D", "JD", "4D", "2C", "8S", "9S", "KC", "6H", "QH", "5H", "3C", "3S", "AC", "AD", "TH", "AS", "TD", "8D", "TC", "8C", "8H", "6D", "7S", "9H"]}',  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ["4C"]

    def test_medium_aggression(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=["QD"],  # Example cards played in the trick
        )

        mock_match_state = MatchState(
            myPlayerNum=1,  # You can mock this as 0
            players=players,  # Empty list for players
            # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
            myHand=[
                "QS",
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
        assert action == ["QH"]

    def test_high_aggression(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=["JD"],  # Example cards played in the trick
        )

        # Mock object creation with only myHand being relevant
        mock_match_state = MatchState(
            myPlayerNum=0,  # You can mock this as 0
            players=[],  # Empty list for players
            myHand=["TS", "JD", "JS", "KH"],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=None,  # Empty match history
            myData='{"remaining_deck": ["QD", "2S", "4C", "7H", "JC"]}',  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ["KH"]


class TestAlgorithmTwoCard:
    def test_passing_early_game(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=["4D", "4S"],  # Example cards played in the trick
        )

        mock_match_state = MatchState(
            myPlayerNum=1,  # You can mock this as 0
            players=players,  # Empty list for players
            # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
            myHand=["3C", "4C", "5C", "2D", "2H"],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=matchHistory,  # Empty match history
            myData='{"remaining_deck": ["QD", "JH", "2S", "7H", "JC", "KS", "2D", "JD", "4D", "2C", "8S", "9S", "KC", "6H", "QH", "5H", "3C", "3S", "AC", "AD", "TH", "AS", "TD", "8D", "TC", "8C", "8H", "6D", "7S", "9H"]}',  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == []


class TestAlgorithmThreeCard:
    def test_passing_early_game(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=["4D", "4S", "4C"],  # Example cards played in the trick
        )

        mock_match_state = MatchState(
            myPlayerNum=1,  # You can mock this as 0
            players=players,  # Empty list for players
            # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
            myHand=["3C", "4H", "2C", "2D", "2H"],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=matchHistory,  # Empty match history
            myData='{"remaining_deck": ["QD", "JH", "2S", "7H", "JC", "KS", "2D", "JD", "4D", "2C", "8S", "9S", "KC", "6H", "QH", "5H", "3C", "3S", "AC", "AD", "TH", "AS", "TD", "8D", "TC", "8C", "8H", "6D", "7S", "9H"]}',  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == []

class TestAlgorithmFiveCard:
    def test_play_straight_first_move(self):
        mock_match_state = MatchState(
            myPlayerNum=1,  # You can mock this as 0
            players=players,  # Empty list for players
            # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
            myHand=["3C", "4C", "5C", "6S", "7S"],  # Example hand
            toBeat=None,  # No need to define, set as None
            matchHistory=matchHistory,  # Empty match history
            myData='',  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ["3C", "4C", "5C", "6S", "7S"]

    def test_play_stronger_straight(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=["3S", "4S", "5S", "6D", "7D"],  # Example cards played in the trick
        )

        mock_match_state = MatchState(
            myPlayerNum=1,  # You can mock this as 0
            players=players,  # Empty list for players
            # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
            myHand=["3C", "4C", "5C", "6S", "7S"],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=matchHistory,  # Empty match history
            myData='',  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ["3C", "4C", "5C", "6S", "7S"]

    def test_play_stronger_5_card_trick(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=["3S", "4S", "5S", "6S", "8S"],  # Example cards played in the trick
        )

        mock_match_state = MatchState(
            myPlayerNum=1,  # You can mock this as 0
            players=players,  # Empty list for players
            # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
            myHand=["4C", "4S", "4D", "7D", "7S"],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=matchHistory,  # Empty match history
            myData='',  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == ["4D", "4C", "4S", "7D", "7S"]

    def test_pass_weaker_5_card_trick(self):
        mock_trick = Trick(
            playerNum=1,  # Mock player number, for example player 1
            cards=['3H', '3S', '9D', '9C', '9S'],  # Example cards played in the trick
        )

        mock_match_state = MatchState(
            myPlayerNum=1,  # You can mock this as 0
            players=players,  # Empty list for players
            # myHand=['KD', '3H', '5C', '5S', '6C', '7S', '7D', '7C', 'TS', 'JS', 'QC'],  # Example hand
            myHand=['4D', '4C', '4S', '2D', '2C'],  # Example hand
            toBeat=mock_trick,  # No need to define, set as None
            matchHistory=matchHistory,  # Empty match history
            myData='',  # Empty string for myData
        )
        algo = Algorithm()
        action, myData = algo.getAction(state=mock_match_state)
        assert action == []
