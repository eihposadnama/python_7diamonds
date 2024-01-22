from Cards import *


class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.extend(card)

    def __str__(self):
        return ', '.join(map(str, self.cards))

    def sort_cards(self):
        # Define a custom sorting key to sort by suit and rank (Ace as low)
        suits_order = {'Diamonds': 0, 'Clubs': 1, 'Hearts': 2, 'Spades': 3}
        self.cards.sort(key=lambda card: (suits_order.get(card.suit, 4), 'A2345678910JQK'.index(card.rank)))

    def has_won(self):
        return len(self.cards) == 0

    def can_play_card_in_hand(self, table):
        for card in self.cards:
            if table.can_play_card(card):
                return True
        return False

    def play_card(self, table, card_index):
        if 0 <= card_index < len(self.cards):
            card_to_play = self.cards.pop(card_index)
            table.add_card(card_to_play)
            return card_to_play
        else:
            print("Invalid card index")
            return None

    def get_hand_string(self):
        return ', '.join(map(str, self.cards))

    def get_card(self, index):
        return self.cards[index]

    def get_length(self):
        return len(self.cards)

    def find_card_index(self, card):
        for i, c in enumerate(self.cards):
            if c.rank == card.rank and c.suit == card.suit:
                return i
        return None

    def find_seven_of_diamonds(self):
        for i, c in enumerate(self.cards):
            if c.rank == '7' and c.suit == "Diamonds":
                return i
        return None
