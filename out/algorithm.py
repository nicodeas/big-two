from classes import *
from itertools import combinations
import json
import math

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
        return strength[rank]

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
        return (Rank.strength(card.rank)-1)*4 + Suit.strength(card.suit)-1
    
    def suit_strength(card):
        assert isinstance(card, Card)
        return (Rank.strength(card.rank))-1 + (Suit.strength(card.suit)-1)*13

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
    def sort_by_suit_strength(cards: list[Card]) -> list[Card]:
        return sorted(cards, key=lambda x: Card.suit_strength(x))
    
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

        # Generate all 3-card combinations
        for combo in combinations(cards, 2):
            if combo[0].rank == combo[1].rank:
                tricks.append(combo)
                value += sum(Card.strength(card) for card in combo)
        
        return tricks, value * Hand.TWO_CARD_STRENGTH_MULTIPLIER

    @staticmethod
    def get_3_card_tricks(
        cards: list[Card],
    ) -> tuple[list[tuple[Card, Card, Card]], int]:
        # count numer of cards per rank
        # if 3 cards -> 1 combination
        # 4 cards -> 4C3 combinations = 4 (if 4 cards, u have a four of a kind)
        # https://docs.python.org/3/library/itertools.html#itertools.combinations
        cards.sort(key=lambda x: Card.strength(x))
        tricks: list[tuple[Card, Card, Card]] = []
        value = 0
        
        # Generate all 3-card combinations
        for combo in combinations(cards, 3):
            if combo[0].rank == combo[1].rank == combo[2].rank:
                tricks.append(combo)
                value += sum(Card.strength(card) for card in combo)

        return tricks, value * Hand.THREE_CARD_STRENGTH_MULTIPLIER


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
        self.state = state
        self.decode()
        
        self.rounds_played = state.matchHistory[-1].gameHistory if state.matchHistory  else []
        # self.round = len(self.rounds_played)-1

    @staticmethod
    def generate_deck():
        deck = set()
        for r in Rank.ranks:
            for s in Suit.suits:
                deck.add(Card(r+s))
        return deck
    
    def generate_deck_from_data(self):
        card_data = self.state.myData['remaining_deck']
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

    def encode(self):
        myData = {}
        myData['remaining_deck'] = [str(card) for card in self.remaining_deck]
        return myData

    def decode(self):
        if 'remaining_deck' in self.state.myData:
            self.remaining_deck = self.generate_deck_from_data()
        else:
            self.remaining_deck = self.generate_deck()
            [self.remove_card(card) for card in self.hand]
            

    def __repr__(self):
        # convert this to a data object we can send and receive back for each game
        myData = self.encode()
        json_data = json.dumps(myData)
        return json_data
    

class Match:
    # maybe make another class for Game, each Match has 3 games
    # keep track of points for each player
    # for each game, keep track of what cards are left in the game, and which ones are not in ur hand
    # how many cards the other players have left
    def __init__(self):
        pass

def is_one_card_trick_stronger(trick1: list[Card], trick2: list[Card]):
    return Card.strength(trick1[0]) > Card.strength(trick2[0])

def is_two_card_trick_stronger(trick1: list[Card], trick2: list[Card]):
    trick1_strength = max(Card.strength(trick1[0]), Card.strength(trick1[1]))
    trick2_strength = max(Card.strength(trick2[0]), Card.strength(trick2[1]))
    
    return trick1_strength > trick2_strength

def is_three_card_trick_stronger(trick1: list[Card], trick2: list[Card]):
    return trick1[0] > trick2[0]

def is_trick_stronger(trick1: list[Card], trick2: list[Card]):
    size = len(trick2)
    if size == 1:
        return is_one_card_trick_stronger(trick1, trick2)
    elif size == 2:
        return is_two_card_trick_stronger(trick1, trick2)
    elif size == 3:
        return is_three_card_trick_stronger(trick1, trick2)

    return False

def get_trick_value(trick):
    pass


def get_valid_tricks_one(cards: list[Card], trick_to_beat: list[Card]) -> list[list[Card]]:
    tricks = [[c] for c in Hand.sort_by_strength(cards)]
    valid_tricks = []

    for trick in tricks:
        if is_trick_stronger(trick, trick_to_beat):
            valid_tricks.append(trick)

    return valid_tricks

def calculate_aggression_one(remaining_cards: int) -> float:
    # Parameters
    max_cards = 39  # Starting number of cards (52 - 13) start of game
    min_cards = 4   # Lowest number of cards (1 for each player)
    
    # Normalize the number of remaining cards to a range from 0 to 1
    normalized_cards = (max_cards - remaining_cards) / (max_cards - min_cards)
    # Parameters for the sigmoid function
    scaling_factor = 0.05  # Scaling factor to control the growth
    growth_rate = 6.0  # Rate of growth
    
    # Calculate sigmoid function
    aggression = min(scaling_factor * (math.exp(growth_rate * normalized_cards) - 1), 1)
    
    return aggression

def calculate_trick_strength_one(trick: list[Card], possible_tricks: list[list[Card]]) -> float:
    num_beaten = sum(1 for opponent_trick in possible_tricks if is_trick_stronger(opponent_trick, trick))
    probability_of_beaten = num_beaten / len(possible_tricks)

    return probability_of_beaten


def one_card_trick(state: Game) -> list[Card]:
    remaining_deck: list[Card] = list(state.remaining_deck)

    trick_to_beat = state.state.toBeat.cards
    valid_tricks = get_valid_tricks_one(state.hand.cards, trick_to_beat)
    if not valid_tricks: 
        print("No valid cards")
        return []

    # Add algorithm below
    aggression = calculate_aggression_one(len(remaining_deck))
    print(f"Aggression value is: {aggression} for {len(remaining_deck)} num of cards")
    possible_tricks = [[card] for card in remaining_deck]
    trick_probabilities = [calculate_trick_strength_one(trick, possible_tricks) for trick in valid_tricks]
    print(valid_tricks)
    print(trick_probabilities)

    if (aggression > 0.9):
            # if game is near end game then play your strongest card
        for i, trick in enumerate(valid_tricks):
            # if game is getting closer to end game then play a strong card
            if trick_probabilities[i] <= 0.2: 
                return trick
            
        return valid_tricks[-1]

    if (aggression > 0.7):
        for i, trick in enumerate(valid_tricks):
            # if game is getting closer to end game then play a strong card
            if trick_probabilities[i] <= 0.35: 
                return trick
            
    if (aggression > 0.25):
        # To give cards priority
        for i, trick in enumerate(valid_tricks):
            # if in mid game the card can be beaten by a large portion of cards, discard it
            if trick_probabilities[i] > 0.7: 
                return trick
            
            # Else, play a stronger than average card
            if trick_probabilities[i] <= 0.4: 
                return trick
        
        # if neither then just play the lowest valid trick
        return valid_tricks[0]
            
        
            
    for i, trick in enumerate(valid_tricks):
        # if the card can be beaten by 40% of the cards during early game
        if trick_probabilities[i] >= 0.4: 
            return trick
            
    return []





def get_valid_tricks_two(cards: list[Card], trick_to_beat: list[Card]) -> list[list[Card]]:
    tricks, _ = Hand.get_2_card_tricks(cards)
    valid_tricks = []

    for trick in tricks:
        if is_trick_stronger(trick, trick_to_beat):
            valid_tricks.append(trick)

    return valid_tricks

def calculate_aggression_two(remaining_cards: int) -> float:
    # Parameters
    max_cards = 39  # Starting number of cards (52 - 13) start of game
    min_cards = 4   # Lowest number of cards (1 for each player)
    
    # Normalize the number of remaining cards to a range from 0 to 1
    normalized_cards = (max_cards - remaining_cards) / (max_cards - min_cards)
    # Parameters for the sigmoid function
    scaling_factor = 0.05  # Scaling factor to control the growth
    growth_rate = 6.0  # Rate of growth
    
    # Calculate sigmoid function
    aggression = min(scaling_factor * (math.exp(growth_rate * normalized_cards) - 1), 1)
    
    return aggression

def calculate_trick_strength_two(trick: list[Card], possible_tricks: list[list[Card]]) -> float:
    num_beaten = sum(1 for opponent_trick in possible_tricks if is_trick_stronger(opponent_trick, trick))
    probability_of_beaten = num_beaten / len(possible_tricks)

    return probability_of_beaten


def two_card_trick(state: Game) -> list[Card]:
    remaining_deck = list(state.remaining_deck)
    # state.state.toBeat.cards = Hand.to_cards(state.state.toBeat.cards) # NOTE: should be done already
    trick_to_beat = state.state.toBeat.cards
    valid_tricks = get_valid_tricks_two(state.hand.cards, trick_to_beat)
    if not valid_tricks: 
        print("No valid cards")
        return []

    # Add algorithm below
    aggression = calculate_aggression_two(len(remaining_deck))
    print(f"Aggression value is: {aggression} for {len(remaining_deck)} num of cards")
    possible_tricks, _ = Hand.get_2_card_tricks(remaining_deck)
    # return []
    trick_probabilities = [calculate_trick_strength_two(trick, possible_tricks) for trick in valid_tricks]
    print(valid_tricks)
    print(trick_probabilities)
    
    if (aggression > 0.9):
            # if game is near end game then play your strongest card
        for i, trick in enumerate(valid_tricks):
            # if game is getting closer to end game then play a strong card
            if trick_probabilities[i] <= 0.2: 
                return trick
            
        return valid_tricks[-1]

    if (aggression > 0.7):
        for i, trick in enumerate(valid_tricks):
            # if game is getting closer to end game then play a strong card
            if trick_probabilities[i] <= 0.35: 
                return trick
            
    if (aggression > 0.25):
        # To give cards priority
        for i, trick in enumerate(valid_tricks):
            # if in mid game the card can be beaten by a large portion of cards, discard it
            if trick_probabilities[i] > 0.7: 
                return trick
            
            # Else, play a stronger than average card
            if trick_probabilities[i] <= 0.4: 
                return trick
        
        # if neither then just play the lowest valid trick
        return valid_tricks[0]
            
        
            
    for i, trick in enumerate(valid_tricks):
        # if the card can be beaten by 40% of the cards during early game
        if trick_probabilities[i] >= 0.4: 
            return trick
            
    return []





def get_valid_tricks_three(cards: list[Card], trick_to_beat: list[Card]) -> list[list[Card]]:
    tricks, _ = Hand.get_3_card_tricks(cards)
    valid_tricks = []

    for trick in tricks:
        if is_trick_stronger(trick, trick_to_beat):
            valid_tricks.append(trick)

    return valid_tricks

def calculate_aggression_three(remaining_cards: int) -> float:
    # Parameters
    max_cards = 39  # Starting number of cards (52 - 13) start of game
    min_cards = 4   # Lowest number of cards (1 for each player)
    
    # Normalize the number of remaining cards to a range from 0 to 1
    normalized_cards = (max_cards - remaining_cards) / (max_cards - min_cards)
    # Parameters for the sigmoid function
    scaling_factor = 0.05  # Scaling factor to control the growth
    growth_rate = 6.0  # Rate of growth
    
    # Calculate sigmoid function
    aggression = min(scaling_factor * (math.exp(growth_rate * normalized_cards) - 1), 1)
    
    return aggression

def calculate_trick_strength_three(trick: list[Card], possible_tricks: list[list[Card]]) -> float:
    num_beaten = sum(1 for opponent_trick in possible_tricks if is_trick_stronger(opponent_trick, trick))
    probability_of_beaten = num_beaten / len(possible_tricks)

    return probability_of_beaten


def three_card_trick(state: Game) -> list[Card]:
    remaining_deck = list(state.remaining_deck)
    # state.state.toBeat.cards = Hand.to_cards(state.state.toBeat.cards) # NOTE: should be done already
    trick_to_beat = state.state.toBeat.cards
    valid_tricks = get_valid_tricks_three(state.hand.cards, trick_to_beat)
    if not valid_tricks: 
        print("No valid cards")
        return []

    # Add algorithm below
    aggression = calculate_aggression_three(len(remaining_deck))
    print(f"Aggression value is: {aggression} for {len(remaining_deck)} num of cards")
    possible_tricks, _ = Hand.get_2_card_tricks(remaining_deck)
    # return []
    trick_probabilities = [calculate_trick_strength_three(trick, possible_tricks) for trick in valid_tricks]
    print(valid_tricks)
    print(trick_probabilities)
    
    if (aggression > 0.9):
            # if game is near end game then play your strongest card
        for i, trick in enumerate(valid_tricks):
            # if game is getting closer to end game then play a strong card
            if trick_probabilities[i] <= 0.2: 
                return trick
            
        return valid_tricks[-1]

    if (aggression > 0.7):
        for i, trick in enumerate(valid_tricks):
            # if game is getting closer to end game then play a strong card
            if trick_probabilities[i] <= 0.35: 
                return trick
            
    if (aggression > 0.25):
        # To give cards priority
        for i, trick in enumerate(valid_tricks):
            # if in mid game the card can be beaten by a large portion of cards, discard it
            if trick_probabilities[i] > 0.7: 
                return trick
            
            # Else, play a stronger than average card
            if trick_probabilities[i] <= 0.4: 
                return trick
        
        # if neither then just play the lowest valid trick
        return valid_tricks[0]
            
        
            
    for i, trick in enumerate(valid_tricks):
        # if the card can be beaten by 40% of the cards during early game
        if trick_probabilities[i] >= 0.4: 
            return trick
            
    return []






def cards_to_strings(func):
    def wrapper(*args, **kwargs):
        action, myData = func(*args, **kwargs)
        action = [str(card) for card in action]
        myData = str(myData)
        # print(f"send data: {len(json.loads(myData)['remaining_deck'])}")
        return action, myData
    return wrapper

class Algorithm:
    def __init__(self):
        self.game = None
        self.state = None

    def start_of_game(self):
        tricks, _ = Hand.get_3_card_tricks(self.game.hand.cards)
        for trick in tricks:
            if Card('3D') in trick:
                return [*trick], self.game
            
        tricks, _ = Hand.get_2_card_tricks(self.game.hand.cards)
        for trick in tricks:
            if Card('3D') in trick:
                return [*trick], self.game
        
        return [Card('3D')], self.game
    
    def first_move(self):
        if Card('3D') in self.game.hand:
            return self.start_of_game()
        
        tricks, _ = Hand.get_3_card_tricks(self.game.hand.cards)
        if (len(tricks)) > 0:
            return [*tricks[0]], self.game

        tricks, _ = Hand.get_2_card_tricks(self.game.hand.cards)
        if (len(tricks)) > 0:
            return [*tricks[0]], self.game
        
        self.game.hand.cards = Hand.sort_by_strength(self.game.hand)
        # print(f"Sorted deck (first move): {self.game.hand.cards}")
        return [self.game.hand.cards[0]], self.game
    
    def one_card_trick(self):
        trick = one_card_trick(self.game)
        return trick, self.game

        tricks = Hand.sort_by_strength(self.game.hand)
        trick_to_beat = self.state.toBeat.cards
        
        print(f"Sorted deck (one card trick): {tricks}")
        for trick in tricks:
            if (is_trick_stronger([trick], trick_to_beat)):
                return [trick], self.game
        
        return self.tempPassMove()

    def two_card_trick(self):
        trick = two_card_trick(self.game)
        return trick, self.game
    
        tricks, _ = Hand.get_2_card_tricks(self.game.hand.cards)
        trick_to_beat = self.state.toBeat.cards

        print(f"(Two card tricks): {tricks}")
        for trick in tricks:
            if (is_trick_stronger(trick, trick_to_beat)):
                return [*trick], self.game

        return self.tempPassMove()

    def three_card_trick(self):
        trick = three_card_trick(self.game)
        return trick, self.game
        tricks, _ = Hand.get_3_card_tricks(self.game.hand.cards)
        trick_to_beat = self.state.toBeat.cards

        print(f"(Three card tricks): {tricks}")
        for trick in tricks:
            if (is_trick_stronger(trick, trick_to_beat)):
                return [*trick], self.game
        
        return self.tempPassMove()

    def five_card_trick(self):
        return self.tempPassMove()

    def tempPassMove(self):
        return [], self.game
    
    @cards_to_strings
    def getAction(self, state: MatchState):
        action = []  # The cards you are playing for this trick
        if not state.myData: state.myData = "{}"
        state.myData = json.loads(state.myData)
        if 'remaining_deck' in state.myData:
            print(f"recv data: {len(state.myData['remaining_deck'])}")

        if (state.toBeat and len(state.toBeat.cards) > 0): 
            state.toBeat.cards = Hand.to_cards(state.toBeat.cards)
        
        # NOTE: Modify state as needed before this

        myData = state.myData  # Communications from the previous iteration
        self.state = state
        self.game = Game(self.state)
        self.game.update_remaining_deck()

        print(f"Cards remaining: {self.game}")
        print(f"My hand:  {self.game.hand.cards}")

        if (not state.toBeat or len(state.toBeat.cards) == 0): 
            return self.first_move()
        
        
        num_of_cards = len(state.toBeat.cards)

        if num_of_cards == 1:
            action, myData = self.one_card_trick()
        elif num_of_cards == 2:
            action, myData = self.two_card_trick()
        elif num_of_cards == 3:
            action, myData = self.three_card_trick()
        else:
            action, myData = self.five_card_trick()
        
        # TODO Write your algorithm logic here

        return action, myData
    

