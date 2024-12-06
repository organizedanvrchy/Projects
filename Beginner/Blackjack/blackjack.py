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

def handle_ace(cards, processed_aces, player_or_dealer="player"):
    ace_changed = False

    for i, card in enumerate(cards):
        if card in [1, 11] and i not in processed_aces:  # Check if the card is an unprocessed Ace
            if player_or_dealer == "player":
                while True:
                    ace = input(f"\nYou were dealt an ACE card. Would you like to use it as a 1 or 11?\nEnter 1 or 11: ").strip()
                    if ace in ["1", "11"]:
                        cards[i] = int(ace)
                        ace_changed = True
                        processed_aces.add(i)  # Mark this Ace as processed
                        break
                    else:
                        print("\nInvalid choice. Please enter 1 or 11.")
            elif player_or_dealer == "dealer":
                cards[i] = dealer_ace_choice(sum(cards))
                ace_changed = True
                processed_aces.add(i)  # Mark this Ace as processed

    return cards, ace_changed


def main():
    player_processed_aces = set()
    dealer_processed_aces = set()

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

        # Handle initial aces for player and dealer
        player_cards, player_ace_changed = handle_ace(player_cards, player_processed_aces, "player")
        dealer_cards, dealer_ace_changed = handle_ace(dealer_cards, dealer_processed_aces, "dealer")

        # Show cards again after ace handling
        if player_ace_changed or dealer_ace_changed:
            display_cards(player_cards, dealer_cards)
        else:
            display_cards(player_cards, dealer_cards)

        # Calculate player's and dealer's scores
        player_score = sum(player_cards)
        dealer_score = sum(dealer_cards)

        # Check if player intially busts
        if player_score > 21:
            print("\nBust! You lose...")
            play = False

        hit = True
        while(hit):
            hit_or_stand = input("\nEnter 'Y' if you choose to HIT or enter 'N' if you choose to STAND. Y or N: ").upper()
            if hit_or_stand == "Y":
                # Player Logic
                player_next_card = deal_card()
                if 1 < player_next_card < 11:
                    print(f"\nYou were dealt a(n) {player_next_card}.")
                player_cards.append(player_next_card)
                # Handle new Aces dealt
                if player_next_card == 1 or player_next_card == 11:
                    player_cards, player_ace_changed = handle_ace(player_cards, player_processed_aces, "player")

                display_cards(player_cards, dealer_cards)

                player_score = sum(player_cards)

                # Check if player busts after new card
                if player_score > 21:
                    print("\nBust! You lose...")
                    hit = False

                # Check if player has a 5 Card Charlie
                if len(player_cards) == 5 and player_score <= 21:
                    print("\nFive Card Charlie! You Win!")
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
                dealer_cards, dealer_ace_changed = handle_ace(dealer_cards, dealer_processed_aces, "dealer")
            dealer_score = sum(dealer_cards)
            
        display_cards(player_cards, dealer_cards, reveal_dealer=True)
        
        # Win/Lose Conditions
        if player_score> 21:
            break
        elif dealer_score > 21:
            print("\nDealer Busts! You Win.")
        elif player_score > dealer_score and player_score <= 21:
            print("\nCongratulations! You Win!")
        elif player_score == dealer_score:
            print(f"\nIt's a Draw! You both scored: {player_score}")

        play_again = input("\nWould you like to play again? Y or N: ").upper()
        if play_again != "Y":
            print("\nThank you for playing! Goodbye...")
            time.sleep(2)
            play = False

if __name__ == "__main__":
    main()
