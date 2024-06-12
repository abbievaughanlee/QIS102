# dealer_fast.py

import time

import numpy as np

# fmt: off
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

ranks = ["Deuce", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
# fmt: on

#creates a deck of shuffled cards
def init_deck():
    #creates an ordered deck
    deck = np.arange(52)
    #"physically" shuffles the ordered cards by assigning them each a new position
    for card_pos in range(52):
        new_card_pos = np.random.randint(52)
        swap_card = deck[card_pos]
        deck[card_pos] = deck[new_card_pos]
        deck[new_card_pos] = swap_card
    return deck


def print_deck(deck):
    for card_pos in range(52):
        card_num = deck[card_pos]
        suit_num = card_num // 13
        rank_num = card_num % 13
        card_name = f"{ranks[rank_num]} of {suits[suit_num]}"
        print(f"The card in position {card_pos} is the {card_name}")

def check_multiples(deck):
    for i in range(0, 52):
        for j in range(i + 1, 52):
            if deck[i] == deck[j]:
                print("deck contains multiples")
                break
    print("deck contains no multiples")


#deal 10000 deals and measure the time it takes to do so
def main():
    np.random.seed(2016)
    total_deals = 10_000

    start_time = time.perf_counter()
    for _ in range(total_deals):
        deck = init_deck()
    elapsed_time = time.perf_counter() - start_time

    print_deck(deck)

    check_multiples(deck)
    
    print(f"Total deals: {total_deals:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}\n")


main()
