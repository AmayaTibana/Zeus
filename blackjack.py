# ============================================================
# BLACKJACK (21) - Player vs. Computer Dealer
# ------------------------------------------------------------
# The goal of Blackjack is to get a hand of cards whose total
# is closer to 21 than the dealer's hand, without going over 21.
#   - Number cards (2-10) are worth their number.
#   - Face cards (J, Q, K) are worth 10.
#   - An Ace is worth 11, or 1 if 11 would make the hand go over 21.
# The player starts with 100 chips, bets on each hand, and plays
# until they choose to stop or run out of chips.
# Every hand is saved to a log file (blackjack_log.txt) so the
# player can review their results later.
# ============================================================

# "random" lets the program shuffle the deck of cards.
import random

# "datetime" lets the program record the date and time in the log file.
from datetime import datetime

# The four suits and thirteen ranks used to build a standard 52-card deck.
SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Game settings that can be changed in one place.
STARTING_CHIPS = 100      # Chips the player begins with
DEALER_STANDS_ON = 17     # The dealer must keep drawing until reaching 17 or more
RESHUFFLE_POINT = 15      # Use a fresh deck when fewer than 15 cards are left
LOG_FILE = "blackjack_log.txt"


# ------------------------------------------------------------
# The Card class represents one playing card, like "K of Hearts".
# ------------------------------------------------------------
class Card:

    # Create a card with a rank (such as "7" or "K") and a suit.
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # Return how many points this card is worth.
    # Aces return 11 here; the Hand class lowers them to 1 when needed.
    def value(self):
        if self.rank in ["J", "Q", "K"]:
            return 10
        elif self.rank == "A":
            return 11
        else:
            return int(self.rank)

    # Return the card as readable text, for example "A of Spades".
    def __str__(self):
        return self.rank + " of " + self.suit


# ------------------------------------------------------------
# The Deck class represents the full 52-card deck.
# ------------------------------------------------------------
class Deck:

    # Build a new deck and shuffle it right away.
    def __init__(self):
        self.cards = []
        self.build()

    # Create one card for every suit and rank combination (4 x 13 = 52),
    # then shuffle them into a random order.
    def build(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(rank, suit))
        random.shuffle(self.cards)

    # Take the top card off the deck and hand it out.
    def deal(self):
        return self.cards.pop()

    # Tell the program how many cards are still in the deck.
    def cards_left(self):
        return len(self.cards)


# ------------------------------------------------------------
# The Hand class holds the cards for one person (player or dealer)
# and knows how to add up their total.
# ------------------------------------------------------------
class Hand:

    # Start with an empty hand.
    def __init__(self):
        self.cards = []

    # Put a new card into the hand.
    def add_card(self, card):
        self.cards.append(card)

    # Add up the hand's total points.
    # First, every Ace counts as 11. Then, while the total is over 21
    # and there is still an Ace counted as 11, change that Ace to 1
    # by subtracting 10. This is how two Aces become 12 instead of 22.
    def get_value(self):
        total = 0
        aces = 0
        for card in self.cards:
            total += card.value()
            if card.rank == "A":
                aces += 1
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1
        return total

    # A "Blackjack" is exactly 21 using only the first two cards.
    def is_blackjack(self):
        return len(self.cards) == 2 and self.get_value() == 21

    # A hand "busts" (automatically loses) when it goes over 21.
    def is_bust(self):
        return self.get_value() > 21

    # Show every card in the hand, separated by commas.
    def __str__(self):
        card_names = []
        for card in self.cards:
            card_names.append(str(card))
        return ", ".join(card_names)


# ------------------------------------------------------------
# Ask the player how many chips to bet.
# Keeps asking until the player types a whole number between
# 1 and the number of chips they have.
# ------------------------------------------------------------
def get_bet(chips):
    while True:
        user_input = input("You have " + str(chips) + " chips. How many do you want to bet? ")
        # Try to turn what the player typed into a whole number.
        try:
            bet = int(user_input)
        except ValueError:
            # The player typed letters, symbols, or a decimal.
            print("Please enter a whole number (for example: 10).")
            continue
        # Make sure the bet is at least 1 and not more than they have.
        if bet < 1:
            print("Your bet must be at least 1 chip.")
        elif bet > chips:
            print("You cannot bet more chips than you have.")
        else:
            return bet


# ------------------------------------------------------------
# Ask the player a question that must be answered with one of
# two letters (for example "h" for hit or "s" for stand).
# Upper or lower case both work, and extra spaces are ignored.
# ------------------------------------------------------------
def get_choice(question, option1, option2):
    while True:
        answer = input(question).strip().lower()
        if answer == option1 or answer == option2:
            return answer
        print("Please type '" + option1 + "' or '" + option2 + "'.")


# ------------------------------------------------------------
# Print both hands. While the player is still deciding, one of
# the dealer's cards stays hidden (face down), like at a real table.
# ------------------------------------------------------------
def show_hands(player_hand, dealer_hand, hide_dealer_card):
    print()
    if hide_dealer_card:
        print("Dealer's hand: " + str(dealer_hand.cards[0]) + ", [hidden card]")
    else:
        print("Dealer's hand: " + str(dealer_hand) + "  (total " + str(dealer_hand.get_value()) + ")")
    print("Your hand:     " + str(player_hand) + "  (total " + str(player_hand.get_value()) + ")")


# ------------------------------------------------------------
# Play one full hand of Blackjack.
# Returns two things: the result ("win", "loss", or "push" for a tie)
# and how many chips the player won (positive) or lost (negative).
# ------------------------------------------------------------
def play_round(deck, chips):
    # Start with a fresh deck if the current one is running low.
    if deck.cards_left() < RESHUFFLE_POINT:
        print("\nShuffling a new deck...")
        deck.build()

    bet = get_bet(chips)

    # Deal two cards to each side, one at a time, player first.
    player_hand = Hand()
    dealer_hand = Hand()
    for i in range(2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

    show_hands(player_hand, dealer_hand, True)

    # --- Check for a Blackjack on the first two cards ---
    if player_hand.is_blackjack() or dealer_hand.is_blackjack():
        show_hands(player_hand, dealer_hand, False)
        if player_hand.is_blackjack() and dealer_hand.is_blackjack():
            print("Both you and the dealer have Blackjack. It's a push (tie).")
            return "push", 0
        elif player_hand.is_blackjack():
            # A Blackjack pays 3 to 2 (bet 10, win 15).
            winnings = int(bet * 1.5)
            print("BLACKJACK! You win " + str(winnings) + " chips.")
            return "win", winnings
        else:
            print("The dealer has Blackjack. You lose " + str(bet) + " chips.")
            return "loss", -bet

    # --- Player's turn: hit (take a card) or stand (stop) ---
    # The loop ends when the player stands, busts, or reaches 21.
    while player_hand.get_value() < 21:
        choice = get_choice("Do you want to (h)it or (s)tand? ", "h", "s")
        if choice == "h":
            new_card = deck.deal()
            player_hand.add_card(new_card)
            print("You drew: " + str(new_card))
            show_hands(player_hand, dealer_hand, True)
        else:
            break

    # If the player went over 21, they lose right away.
    if player_hand.is_bust():
        print("You busted with " + str(player_hand.get_value()) + ". You lose " + str(bet) + " chips.")
        return "loss", -bet

    # --- Dealer's turn: reveal the hidden card, then draw until 17+ ---
    print("\nDealer reveals the hidden card.")
    show_hands(player_hand, dealer_hand, False)
    while dealer_hand.get_value() < DEALER_STANDS_ON:
        new_card = deck.deal()
        dealer_hand.add_card(new_card)
        print("Dealer draws: " + str(new_card) + "  (dealer total " + str(dealer_hand.get_value()) + ")")

    # --- Compare the final totals ---
    player_total = player_hand.get_value()
    dealer_total = dealer_hand.get_value()

    if dealer_hand.is_bust():
        print("The dealer busted with " + str(dealer_total) + ". You win " + str(bet) + " chips!")
        return "win", bet
    elif player_total > dealer_total:
        print("Your " + str(player_total) + " beats the dealer's " + str(dealer_total) + ". You win " + str(bet) + " chips!")
        return "win", bet
    elif player_total < dealer_total:
        print("The dealer's " + str(dealer_total) + " beats your " + str(player_total) + ". You lose " + str(bet) + " chips.")
        return "loss", -bet
    else:
        print("You both have " + str(player_total) + ". It's a push (tie). Your bet is returned.")
        return "push", 0


# ------------------------------------------------------------
# Write one line to the log file describing a hand that was played.
# "a" means append: new lines are added to the end of the file,
# so the history of earlier games is kept.
# ------------------------------------------------------------
def log_hand(hand_number, result, change, chips):
    now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open(LOG_FILE, "a") as file:
        file.write(now + " | Hand " + str(hand_number) + " | Result: " + result +
                   " | Chips won/lost: " + str(change) + " | Chips after hand: " + str(chips) + "\n")


# ------------------------------------------------------------
# Write the end-of-session summary to the log file.
# ------------------------------------------------------------
def log_summary(wins, losses, pushes, chips):
    hands = wins + losses + pushes
    with open(LOG_FILE, "a") as file:
        file.write("SESSION SUMMARY | Hands: " + str(hands) + " | Wins: " + str(wins) +
                   " | Losses: " + str(losses) + " | Pushes: " + str(pushes) +
                   " | Final chips: " + str(chips) + "\n\n")


# ------------------------------------------------------------
# The main function is where the program starts.
# It keeps track of the chips and the score, and keeps playing
# hands until the player quits or runs out of chips.
# ------------------------------------------------------------
def main():
    print("=========================================")
    print("        Welcome to Blackjack (21)!       ")
    print("=========================================")
    print("Get closer to 21 than the dealer without going over.")
    print("Face cards are worth 10. Aces are worth 11 or 1.")
    print("The dealer must draw until reaching 17 or more.")
    print("A Blackjack (21 with your first two cards) pays 3 to 2.")

    # Starting values for the session.
    deck = Deck()
    chips = STARTING_CHIPS
    wins = 0
    losses = 0
    pushes = 0
    hand_number = 0

    # Keep playing while the player still has chips.
    while chips > 0:
        hand_number += 1
        print("\n----------- Hand " + str(hand_number) + " -----------")

        result, change = play_round(deck, chips)

        # Update the chip count and the score.
        chips += change
        if result == "win":
            wins += 1
        elif result == "loss":
            losses += 1
        else:
            pushes += 1

        log_hand(hand_number, result, change, chips)
        print("You now have " + str(chips) + " chips.")

        # Stop automatically if the player is out of chips.
        if chips == 0:
            print("\nYou are out of chips. Game over!")
            break

        # Otherwise, ask whether to play another hand.
        again = get_choice("\nPlay another hand? (y/n) ", "y", "n")
        if again == "n":
            break

    # Show the final results of the session.
    hands_played = wins + losses + pushes
    print("\n============= FINAL RESULTS =============")
    print("Hands played: " + str(hands_played))
    print("Wins: " + str(wins) + "   Losses: " + str(losses) + "   Pushes: " + str(pushes))
    if hands_played > 0:
        win_percentage = wins / hands_played * 100
        print("Winning percentage: " + str(round(win_percentage, 1)) + "%")
    print("Final chips: " + str(chips) + " (started with " + str(STARTING_CHIPS) + ")")
    print("Your results were saved to " + LOG_FILE + ".")

    log_summary(wins, losses, pushes, chips)


# Run the main function only when this file is run directly.
if __name__ == "__main__":
    main()