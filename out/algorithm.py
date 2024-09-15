from classes import *
import json

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

class Suit:
    D = "D"
    C = "C"
    H = "H"
    S = "S"

    suits = [D, C, H, S]

    @staticmethod
    def strength(suit):
        strength = {Suit.D: 1, Suit.C: 2, Suit.H: 3, Suit.S: 4}
        return strength[suit]

class Card:
    rank: str
    suit: str
    rank_mapping = {
        "3": Rank._3,
        "4": Rank._4,
        "5": Rank._5,
        "6": Rank._6,
        "7": Rank._7,
        "8": Rank._8,
        "9": Rank._9,
        "T": Rank.T,
        "J": Rank.J,
        "Q": Rank.Q,
        "K": Rank.K,
        "A": Rank.A,
        "2": Rank._2,
    }
    suit_mapping = {"D": Suit.D, "C": Suit.C, "H": Suit.H, "S": Suit.S}

    def __init__(self, card: str) -> None:
        self.rank = self.rank_mapping[card[0]]
        self.suit = self.suit_mapping[card[1]]

    @staticmethod
    def strength(card):
        assert isinstance(card, Card)
        return Rank.strength(card.rank) + Suit.strength(card.suit)

    def __eq__(self, other) -> bool:
        assert isinstance(other, Card)
        return self.rank == other.rank and self.suit == other.suit

    def __gt__(self, other) -> bool:
        assert isinstance(other, Card)
        if Rank.strength(self.rank) > Rank.strength(other.rank):
            return True
        elif Rank.strength(self.rank) < Rank.strength(other.rank):
            return False
        elif Suit.strength(self.suit) > Suit.strength(other.suit):
            return True
        return False

    def __lt__(self, other) -> bool:
        assert isinstance(other, Card)
        if Rank.strength(self.rank) < Rank.strength(other.rank):
            return True
        elif Rank.strength(self.rank) > Rank.strength(other.rank):
            return False
        elif Suit.strength(self.suit) < Suit.strength(other.suit):
            return True
        return False
    
    def __hash__(self) -> int:
        return hash(f"{self.rank}{self.suit}")

    def __repr__(self) -> str:
        return f"{self.rank}{self.suit}"
    
    def __str__(self) -> str:
        return f"{self.rank}{self.suit}"

class Hand:
    cards: list[Card] = None
    TWO_CARD_STRENGTH_MULTIPLIER = 2
    THREE_CARD_STRENGTH_MULTIPLIER = 4
    STRAIGHT_STRENGTH_MULTIPLIER = 8

    def __init__(self, cards: list[Card] | list[str]) -> None:
        self.cards = self.to_cards(cards)

    @staticmethod
    def sort_by_suit(cards: list[Card]) -> list[Card]:
        return sorted(cards, key=lambda x: Suit.strength(x.suit))

    @staticmethod
    def sort_by_rank(cards: list[Card]) -> list[Card]:
        return sorted(cards, key=lambda x: Rank.strength(x.rank))
    
    @staticmethod
    def sort_by_strength(cards: list[Card]) -> list[Card]:
        return sorted(cards, key=lambda x: Card.strength(x))
    
    @staticmethod
    def to_cards(cards: list[Card] | list[str]) -> list[Card]:
        return [Card(str(c)) for c in cards]
    
    def get_hand(self) -> list[Card]:
        return self.cards

    def get_hand_strength(self):
        pass

    @staticmethod
    def get_2_card_tricks(cards: list[Card]) -> tuple[list[tuple[Card, Card]], int]:
        cards.sort(key=lambda x: Card.strength(x))
        # TODO: maybe this has a tools that simplify this
        # https://docs.python.org/3/library/itertools.html#itertools
        tricks: list[tuple[Card, Card]] = []
        value = 0
        n = len(cards)
        for i in range(n):
            for j in range(1, n - i):
                if cards[i].rank == cards[i + j].rank:
                    tricks.append((cards[i], cards[i + j]))
                    value += Card.strength(cards[i]) + Card.strength(cards[i + j])
                else:
                    break
        return tricks, value * Hand.TWO_CARD_STRENGTH_MULTIPLIER

    @staticmethod
    def get_3_card_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card]], int]:
        # count numer of cards per rank
        # if 3 cards -> 1 combination
        # 4 cards -> 4C3 combinations = 4 (if 4 cards, u have a four of a kind)
        # https://docs.python.org/3/library/itertools.html#itertools.combinations
        pass

    @staticmethod
    def get_straight_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # TODO: easy
        pass

    @staticmethod
    def get_flush_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # TODO: easy
        pass

    @staticmethod
    def get_full_house_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # many combinations
        pass

    @staticmethod
    def get_four_of_a_kind_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # how to figure out what card to throw away in this?
        pass

    @staticmethod
    def get_straight_flush_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # get straight trick + check that all same suit
        pass

    @staticmethod
    def get_5_card_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card, Card, Card]], int]:
        # maybe return as a dictionary with keys 1, 2, 3, 4, 5 for relative strength of 5 card tricks
        # might make it easier to compare against

        # TODO: weakest(top) to strongest (bottom)
        # get_straight_tricks
        # get_flush_tricks
        # get_full_house_tricks
        # get_four_of_a_kind_tricks
        # get_straight_flush_tricks
        pass

    def __iter__(self) -> list[Card]:
        return iter(self.cards)

class Game:
    def __init__(self, state: MatchState):
        # reset the game state with the data object
        self.hand = Hand(state.myHand)
        if len(state.myData) == 0 or True:
            self.remaining_deck = self.generate_deck()
            [self.remove_card(card) for card in self.hand]
        else:
            self.remaining_deck = self.generate_deck_from_data(state.myData)
        self.rounds_played = state.matchHistory[-1].gameHistory if state.matchHistory  else []
        # self.round = len(self.rounds_played)-1

    @staticmethod
    def generate_deck():
        deck = set()
        for r in Rank.ranks:
            for s in Suit.suits:
                deck.add(Card(r+s))
        return deck
    
    @staticmethod
    def generate_deck_from_data(json_data):
        card_data = json.loads(json_data)
        deck = set()
        for card in card_data:
            deck.add(Card(card))
        return deck

        # remove ur cards from the deck and each move keep track of which cards are left
    def update_remaining_deck(self):
        # maybe keep track of the last round only and keep state updated by myData
        for rounds in self.rounds_played:
            for tricks in rounds:
                for card in tricks.cards:
                    self.remove_card(card)

    def remove_card(self, card):
        self.remaining_deck.discard(Card(str(card)))

    def __repr__(self):
        # convert this to a data object we can send and receive back for each game
        json_data = json.dumps([str(card) for card in self.remaining_deck])
        return json_data
    

class Match:
    # maybe make another class for Game, each Match has 3 games
    # keep track of points for each player
    # for each game, keep track of what cards are left in the game, and which ones are not in ur hand
    # how many cards the other players have left
    def __init__(self):
        pass

def is_one_card_trick_stronger(trick1, trick2):
    return Card.strength(trick1[0]) > Card.strength(trick2[0])

def is_two_card_trick_stronger(trick1, trick2):
    trick1_strength = max(Card.strength(trick1[0]), Card.strength(trick1[1]))
    trick2_strength = max(Card.strength(trick2[0]), Card.strength(trick2[1]))
    
    return trick1_strength > trick2_strength

def is_trick_stronger(trick1, trick2):
    size = len(trick2)
    if size == 1:
        return is_one_card_trick_stronger(trick1, trick2)
    elif size == 2:
        return is_two_card_trick_stronger(trick1, trick2)

    return False

def get_trick_value(trick):
    pass



def cards_to_strings(func):
    def wrapper(*args, **kwargs):
        action, myData = func(*args, **kwargs)
        action = [str(card) for card in action]
        myData = str(myData)
        print(f"send data: {len(myData)}")
        print(f"send data: {myData}")
        return action, myData
    return wrapper

class Algorithm:
    def __init__(self):
        self.game = None
        self.state = None

    def start_of_game(self):
        tricks, _ = Hand.get_2_card_tricks(self.game.hand.cards)
        for trick in tricks:
            if Card('3D') in trick:
                return [*trick], self.game
        
        return [Card('3D')], self.game
    
    def first_move(self):
        if Card('3D') in self.game.hand:
            return self.start_of_game()
        
        tricks, _ = Hand.get_2_card_tricks(self.game.hand.cards)
        # print(tricks)
        if (len(tricks)) > 0:
            return [*tricks[0]], self.game
        
        self.game.hand.cards = Hand.sort_by_strength(self.game.hand)
        print(f"Sorted deck (first move): {self.game.hand.cards}")
        return [self.game.hand.cards[0]], self.game
    
    def one_card_trick(self):
        tricks = Hand.sort_by_strength(self.game.hand)
        trick_to_beat = self.state.toBeat.cards
        
        print(f"Sorted deck (one card trick): {tricks}")
        for trick in tricks:
            if (is_trick_stronger([trick], trick_to_beat)):
                return [trick], self.game
        
        return self.tempPassMove()

    def two_card_trick(self):
        tricks, _ = Hand.get_2_card_tricks(self.game.hand.cards)
        trick_to_beat = self.state.toBeat.cards

        print(f"Two card tricks): {tricks}")
        for trick in tricks:
            if (is_trick_stronger(trick, trick_to_beat)):
                return [*trick], self.game


        return self.tempPassMove()

    def three_card_trick(self):
        return self.tempPassMove()

    def five_card_trick(self):
        return self.tempPassMove()

    def tempPassMove(self):
        return [], self.game
    
    @cards_to_strings
    def getAction(self, state: MatchState):
        action = []  # The cards you are playing for this trick
        myData = state.myData  # Communications from the previous iteration
        print(f"recv data: {len(state.myData)}")
        print(f"recv data: {state.myData}")


        self.state = state
        self.game = Game(state)
        self.game.update_remaining_deck()
        print(f"Cards remaining: {self.game}")

        if (not state.toBeat or len(state.toBeat.cards) == 0): 
            return self.first_move()
        
        self.state.toBeat.cards = Hand.to_cards(self.state.toBeat.cards)
        num_of_cards = len(state.toBeat.cards)

        if num_of_cards == 1:
            return self.one_card_trick()
        elif num_of_cards == 2:
            return self.two_card_trick()
        elif num_of_cards == 3:
            return self.three_card_trick()
        else:
            return self.five_card_trick()
        
        # TODO Write your algorithm logic here

        return action, myData
    

