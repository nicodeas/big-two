from algorithm import Card


class TestCard:
    def test_greater_than(self):
        a = Card("2S")
        b = Card("2H")
        c = Card("2S")
        d = Card("KS")
        assert a > b
        assert not a > c
        assert not d > a

    def test_equality(self):
        a = Card("2S")
        b = Card("2S")
        assert a == b
