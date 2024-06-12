# list_cards.py

import numpy as np

# fmt: off
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

ranks = ["Deuce", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
# fmt: on


def init_deck():
    #creates an array from 0 to 51
    return np.arange(52)


def print_deck(deck):
    #iterates through each of the cards and based on their number assigns a card value
    for card_pos in range(52):
        card_num = deck[card_pos]
        suit_num = card_num // 13
        rank_num = card_num % 13
        card_name = f"{ranks[rank_num]} of {suits[suit_num]}"
        print(f"The card in position {card_pos} is the {card_name}")

#creates a deck and prints out the cards
def main():
    deck = init_deck()
    print_deck(deck)


main()
