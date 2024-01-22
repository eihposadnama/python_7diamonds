class Table:

    def __init__(self):
        self.hearts = [None] * 13  # Array to store hearts cards (fixed length of 13)
        self.diamonds = [None] * 13  # Array to store diamonds cards (fixed length of 13)
        self.clubs = [None] * 13  # Array to store clubs cards (fixed length of 13)
        self.spades = [None] * 13  # Array to store spades cards (fixed length of 13)

    def add_card(self, card):
        suit = card.suit
        rank_index = 'A2345678910JQK'.index(card.rank)
        if rank_index>=11:
            rank_index-=1
        #print(f"add card rank index {rank_index}")
        if suit == 'Hearts':
            self.hearts[rank_index] = card
        elif suit == 'Diamonds':
            self.diamonds[rank_index] = card
        elif suit == 'Clubs':
            self.clubs[rank_index] = card
        elif suit == 'Spades':
            self.spades[rank_index] = card
        else:
            print("Invalid suit:", suit)

    def __str__(self):
        table_str = "Cards on the Table:\n"
        table_str += f"Hearts: {', '.join(map(str, filter(None, self.hearts)))}\n"
        table_str += f"Diamonds: {', '.join(map(str, filter(None, self.diamonds)))}\n"
        table_str += f"Clubs: {', '.join(map(str, filter(None, self.clubs)))}\n"
        table_str += f"Spades: {', '.join(map(str, filter(None, self.spades)))}\n"
        return table_str

    def can_play_card(self, card):
        suit = card.suit
        rank_index = 'A2345678910JQK'.index(card.rank)
        if rank_index>=11:
            rank_index-=1

        if suit == 'Hearts':
            if card.rank == '7' or (rank_index >= 7 and self.hearts[rank_index - 1] is not None) or (rank_index < 7 and self.hearts[rank_index + 1] is not None):
                return True
        elif suit == 'Diamonds':
            if card.rank == '7' or (rank_index >= 7 and self.diamonds[rank_index - 1] is not None) or (rank_index < 7 and self.diamonds[rank_index + 1] is not None):
                return True
        elif suit == 'Clubs':
            if card.rank == '7' or (rank_index >= 7 and self.clubs[rank_index - 1] is not None) or (rank_index < 7 and self.clubs[rank_index + 1] is not None):
                return True
        elif suit == 'Spades':
            if card.rank == '7' or (rank_index >= 7 and self.spades[rank_index - 1] is not None) or (rank_index < 7 and self.spades[rank_index + 1] is not None):
                return True

        return False