from Table import Table

from Cards import *
from Deck import *
from Hand import *



def play_game():
    """initialises game"""

    # Create a deck and shuffle it
    deck = Deck()
    deck.shuffle()
    table = Table()

    # Create multiple hands
    num_players = 4
    hands = [Hand() for _ in range(num_players)]

    # Deal and print a hand of 5 cards for each player
    for player in hands:
        player.add_card(deck.deal(13))

    # Find the player with the Seven of Diamonds and make them play first
    seven_of_diamonds_player = None
    found_flag = False
    for i, player in enumerate(hands):
        for j, card in enumerate(player.cards):
            if card.rank == '7' and card.suit == 'Diamonds':
                seven_of_diamonds_player = i
                found_flag = True
                break
        if found_flag:
            break

    hands = hands[seven_of_diamonds_player:] + hands[:seven_of_diamonds_player]

    turn_pointer = 0

    for player in hands:
        player.sort_cards()

    # Print each player's hand
    for i, player in enumerate(hands):
        print(f"Player {i + 1}'s hand: {player}")

    someone_has_won = False
    print("\n")
    print(table)
    print("\n")
    print(f"Player {turn_pointer + 1}  it is your turn, here is your hand")
    print(hands[turn_pointer].get_hand_string())
    print("You have the 7 of diamonds and as such, place it on the table")
    seven_of_diamonds_card_index = hands[turn_pointer].find_seven_of_diamonds()
    hands[turn_pointer].play_card(table, seven_of_diamonds_card_index)
    turn_pointer = (turn_pointer + 1) % num_players

    while not someone_has_won:
        print("\n")
        print(table)
        print("\n")
        print(f"Player {turn_pointer+1}  it is your turn, here is your hand")
        print(hands[turn_pointer].get_hand_string())
        valid_input = False
        if hands[turn_pointer].can_play_card_in_hand(table):
            while not valid_input:
                card_to_be_played = input("Enter type the position of the card you would like to play")
                try:
                    card_to_be_played = int(card_to_be_played)
                    if card_to_be_played > hands[turn_pointer].get_length() or card_to_be_played < 1:
                        print("Index out of range")
                    else:
                        if table.can_play_card(hands[turn_pointer].get_card(card_to_be_played-1)):
                            hands[turn_pointer].play_card(table, card_to_be_played-1)
                            valid_input = True
                        else:
                            print("The index of the card you have just typed can't be played, please try again")
                except:
                    print("Please enter an integer")
        else:
            print(f"Player {turn_pointer+1} can't play any cards so passes")

        if hands[turn_pointer].has_won():
            someone_has_won = True
            print(f"Player {turn_pointer + 1} has won")
        else:
            turn_pointer = (turn_pointer + 1) % num_players


if __name__ == '__main__':
    play_game()
