from Cards import *


class Deck:
    def __init__(self):
        self.ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, num_cards):
        if num_cards <= len(self.cards):
            return [self.cards.pop() for _ in range(num_cards)]
        else:
            return None

    def __str__(self):
        return ', '.join(map(str, self.cards))