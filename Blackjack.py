import random
from utils import clear_console

# Constants
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(hand):
    """Calculate the score of a hand, accounting for Aces."""
    score = sum(hand)
    num_aces = hand.count(11)
    if score == 21 and len(hand) == 2:
        score = 0
    while score > 21 and num_aces:
        score -= 10
        num_aces -= 1
        hand.remove(11)
        hand.append(1)

    return score


def display_hands(your_cards, dealer_hand, reveal_dealer=False):
    """Display the hands of the player and dealer."""
    print(f"Your cards: {your_cards}, Total: {calculate_score(your_cards)}")
    if reveal_dealer:
        print(f"Dealer's cards: {dealer_hand}, Total: {calculate_score(dealer_hand)}")
    else:
        print(f"Dealer's cards: [{dealer_hand[0]}, ?]")


def blackjack_game():
    """Main function to run a single game of Blackjack."""
    while True:
        start = input("Welcome to Blackjack!\nPress 'q' to quit or any other key to play: ")
        if start.lower() == "q":
            print("Thanks for playing!")
            break

        your_cards = [random.choice(CARDS), random.choice(CARDS)]
        dealer_hand = [random.choice(CARDS), random.choice(CARDS)]

        display_hands(your_cards, dealer_hand)

        while calculate_score(your_cards) < 21:
            choice = input("Would you like to 'hit' or 'stand'? ").lower()
            if choice == 'hit':
                your_cards.append(random.choice(CARDS))
                display_hands(your_cards, dealer_hand)
            elif choice == 'stand':
                break

        if calculate_score(your_cards) <= 21:
            while calculate_score(dealer_hand) < 17:
                dealer_hand.append(random.choice(CARDS))

            dealer_score = calculate_score(dealer_hand)
            player_score = calculate_score(your_cards)

            display_hands(your_cards, dealer_hand, reveal_dealer=True)
            if player_score == 0:
                print("You have a blackjack, You win!")
            elif dealer_score == 0:
                print("Sorry, you lost,the dealer has a blackjack")
            elif dealer_score > 21:
                print("Dealer busts. You win!")
            elif player_score > dealer_score:
                print("You win!")
            elif player_score < dealer_score:
                print("You lose!")
            else:
                print("It's a draw!")
            clear = input("Press 'c' to return to main screen: ")
            if clear.lower() == 'c':
                clear_console()
            else:
                break


blackjack_game()
