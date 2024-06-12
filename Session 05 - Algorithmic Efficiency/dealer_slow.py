# dealer_slow.py

import time

import numpy as np

# fmt: off
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

ranks = ["Deuce", "Three", "Four", "Five", "Six", "Seven",
         "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
# fmt: on

#creates a shuffled deck
def init_deck():
    deck = np.arange(52)
    #array of zeroes- boolean treated as a zero is false
    already_dealt = np.zeros(52, dtype=bool)
    #ensures that at each position, if a number has already been assigned then it will not be reassigned
    for card_pos in range(52):
        card_num = np.random.randint(52)
        while already_dealt[card_num]:
            card_num = np.random.randint(52)
        deck[card_pos] = card_num
        already_dealt[card_num] = True
    return deck

#prints the shuffled deck
def print_deck(deck):
    for card_pos in range(52):
        card_num = deck[card_pos]
        suit_num = card_num // 13
        rank_num = card_num % 13
        card_name = f"{ranks[rank_num]} of {suits[suit_num]}"
        print(f"The card in position {card_pos} is the {card_name}")

# check that there are no multiples
# iterate through each card and check that it is not the same as any of the other
def check_multiples(deck):
    for i in range(0, 52):
        for j in range(i + 1, 52):
            if deck[i] == deck[j]:
                print("deck contains multiples")
                break
    print("deck contains no multiples")



#deal 10,000 decks
#time how long it takes to do this
def main():
    np.random.seed(2016)
    total_deals = 10_000

    start_time = time.perf_counter()
    #calls init_deck 10000 times
    for _ in range(total_deals):
        deck = init_deck()
    elapsed_time = time.perf_counter() - start_time

    print_deck(deck)
    check_multiples(deck)
    print(f"Total deals: {total_deals:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}")


main()

