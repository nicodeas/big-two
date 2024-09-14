# MERGE FROM HERE
class Rank:
    _3 = "3"
    _4 = "4"
    _5 = "5"
    _6 = "6"
    _7 = "7"
    _8 = "8"
    _9 = "9"
    T = "T"
    J = "J"
    Q = "Q"
    K = "K"
    A = "A"
    _2 = "2"

    ranks = [_3, _4, _5, _6, _7, _8, _9, T, J, Q, K, A, _2]

    @staticmethod
    def strength(rank):
        strength = {
            Rank._3: 1,
            Rank._4: 2,
            Rank._5: 3,
            Rank._6: 4,
            Rank._7: 5,
            Rank._8: 6,
            Rank._9: 7,
            Rank.T: 8,
            Rank.J: 9,
            Rank.Q: 10,
            Rank.K: 11,
            Rank.A: 12,
            Rank._2: 13,
        }
        # 4x as rank more important than suite
        # maps each card from 1-52 when combined with suit
        return 4 * strength[rank]