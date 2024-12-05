import random
import time
import art

def deal_card():
    # Returns a random card value from the deck (1 to 11).
    return random.randint(1, 11)

def display_cards(player_cards, dealer_cards, reveal_dealer=False):
    # Displays the player's hand
    print(f"\nYour cards: {player_cards} - Score: {sum(player_cards)}")

    # Display dealer's first card only or entire hand (when necessary)
    if reveal_dealer:
        print(f"Dealer's cards: {dealer_cards} - Score: {sum(dealer_cards)}")
    else:
        print(f"Dealer's cards: [{dealer_cards[0]}, ???]")

def dealer_ace_choice(dealer_score):
    if dealer_score + 11 <= 21:
        return 11
    else:
        return 1 

def handle_ace(cards, player_or_dealer="player"):
    # Flag for ace changes
    ace_changed = False

    # Handle ace cards in player's or dealer's hand
    for i in range(len(cards)):
        if cards[i] == 1 or cards[i] == 11:
            if player_or_dealer == "player":
                ace = input(f"\nThis {cards[i]} is an ACE card. Would you like to use it as a 1 or 11?\nEnter 1 or 11: ").strip()
                if ace == "1":
                    cards[i] = 1
                    ace_changed = True
                elif ace == "11":
                    cards[i] = 11
                    ace_changed = True
            elif player_or_dealer == "dealer":
                cards[i] = dealer_ace_choice(sum(cards))
                ace_changed = True
    return cards, ace_changed

def main():
    user_choice = input("\nWelcome. Would you like to play BlackJack? Y or N: ").upper()
    if user_choice != "Y":
        print("\nThank you. Goodbye...\n")
        time.sleep(2)        
        return 0

    play = True
    while play:
        print(art.logo)

        # Intialize player's and dealer's hands
        player_cards = [deal_card(), deal_card()]
        dealer_cards = [deal_card(), deal_card()]

        display_cards(player_cards, dealer_cards)

        # Handle initial aces for player and dealer
        player_cards, player_ace_changed = handle_ace(player_cards, "player")
        dealer_cards, dealer_ace_changed = handle_ace(dealer_cards, "dealer")

        # Show cards again after ace handling
        if player_ace_changed or dealer_ace_changed:
            display_cards(player_cards, dealer_cards)

        # Calculate player's and dealer's scores
        player_score = sum(player_cards)
        dealer_score = sum(dealer_cards)

        # Check if player intially busts
        if player_score > 21:
            print(f"\nYour hand is {player_cards} with a score of : {player_score}!")
            print("Bust! You lose...")
            play = False

        hit = True
        while(hit):
            hit_or_stand = input("\nEnter 'Y' if you choose to HIT or enter 'N' if you choose to STAND. Y or N: ").upper()
            if hit_or_stand == "Y":
                # Player Logic
                player_next_card = deal_card()
                print(f"\nYou were dealt a(n) {player_next_card}.")
                player_cards.append(player_next_card)

                # Handle new Aces dealt
                if player_next_card == 1 or player_next_card == 11:
                    player_cards, player_ace_changed = handle_ace(player_cards, "player")

                display_cards(player_cards, dealer_cards)

                player_score = sum(player_cards)

                # Check if player busts after new card
                if player_score > 21:
                    print(f"\nYour hand is {player_cards} with a score of : {player_score}!")
                    print("Bust! You lose...")
                    hit = False

            elif hit_or_stand == "N":
                hit = False
            else:
                print("\nInvalid selection. Try again...")
                continue

        # Dealer Logic
        while dealer_score < 17:
            dealer_next_card = deal_card()
            dealer_cards.append(dealer_next_card)

            # Handle new Aces dealt
            if dealer_next_card == 1 or dealer_next_card == 11:
                dealer_cards, dealer_ace_changed = handle_ace(dealer_cards, "dealer")
            dealer_score = sum(dealer_cards)
            
        display_cards(player_cards, dealer_cards, reveal_dealer=True)
        
        # Win/Lose Conditions
        if player_score > 21:
            print("\nBust! You Lose...")
        elif dealer_score > 21:
            print("\nDealer Busts! You Win.")
        elif player_score > dealer_score:
            print("\nCongratulations! You Win!")
        elif player_score == dealer_score:
            print(f"\nIt's a Draw! You both scored: {player_score}")
        else:
            print("\nYou Lose...")

        play_again = input("\nWould you like to play again? Y or N: ").upper()
        if play_again != "Y":
            print("\nThank you for playing! Goodbye...")
            time.sleep(2)
            play = False

if __name__ == "__main__":
    main()
