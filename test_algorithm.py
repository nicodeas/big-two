from algorithm import Card


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
