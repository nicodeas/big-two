from algorithm import Card, Hand


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

