from math import fabs
from art import logo
import random

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

############### Blackjack game source code #####################

def blackjack():
    print(logo)
    print("The dealer shuffles the deck and distributes the cards.")

    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player = []
    dealer = []

    def draw(user):
        user.append(random.choice(cards))

    def calculate_score(hand):
        return sum(hand)

    def lose_checker(player_score, dealer_score):
        if player_score > 21:
            print(f"You lose, your score is {player_score}.")
            replay_game(input("Do you want to replay?: [y] or [n]"))
        elif dealer_score > 21:
            print(f"You win, the dealer has a score of {dealer_score}.")
            replay_game(input("Do you want to replay?: [y] or [n]"))

    def win_checker(player_score, dealer_score):
        if player_score == dealer_score:
            print(f"It's a tie, both scores are equal.")
            replay_game(input("Do you want to replay?: [y] or [n]"))
        elif dealer_score > player_score:
            print(f"You lose, your score is {player_score} and the dealer has {dealer_score}.")
            replay_game(input("Do you want to replay?: [y] or [n]"))
        elif player_score > dealer_score:
            print(f"You win, your score is {player_score} and the dealer has {dealer_score}.")
            replay_game(input("Do you want to replay?: [y] or [n]"))

    def replay_game(choice):
        if choice == "y":
            print(logo)
            print("The dealer shuffles the deck and distributes the cards.")
            blackjack()
        if choice == 'n':
            print("Thanks for playing!")
            exit

    def game_loop():
        if len(player) == 0 and len(dealer) == 0:
            draw(player)
            draw(player)
            draw(dealer)
            draw(dealer)
            print(f"The dealer has drawn a {dealer[0]} and the player has drawn a {player[0]} and {player[1]}.")
            print(f"The player's total is {calculate_score(player)}.")
            game_loop()
        else:
            pass_turn = False
            while pass_turn == False:
                hit_me = input("Would you like to draw another card? [y] or [n]: ")
                if hit_me == "y":
                    if calculate_score(dealer) < 16:
                        draw(dealer)
                    draw(player)
                    print(f"You drew a {player[-1]}, your new total is {calculate_score(player)}.")
                    lose_checker(calculate_score(player), calculate_score(dealer))
                else:
                    if calculate_score(dealer) < 16:
                        draw(dealer)
                        lose_checker(calculate_score(player), calculate_score(dealer))
                    win_checker(calculate_score(player), calculate_score(dealer))
                    pass_turn = True
    game_loop()

blackjack()
