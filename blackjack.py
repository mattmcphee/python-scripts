import random, sys

# set up the constants
HEARTS = chr(9829)  # character 9829 is heart
DIAMONDS = chr(9830)  # character 9830 is diamond
SPADES = chr(9824)  # character 9824 is spade
CLUBS = chr(9827)  # character 9827 is club
BACKSIDE = "backside"


def main():
    print("Blackjack")
    money = 5000

    while True:  # main game loop

        # check if player has run out of money
        if money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money!")
            print("Thanks for playing!")
            sys.exit()

        # let the player enter their bet for this round
        print("Money:", money)
        bet = getBet(money)

        # give the dealer and player two cards from the deck each
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # handle player actions
        print("Bet:", bet)
        while True:  # keep looping until player stands or busts
            displayHands(playerHand, dealerHand, False)
            print()

            # check if the player has bust
            if getHandValue(playerHand) > 21:
                break

            # get the player's move, either H, S or D
            move = getMove(playerHand, money - bet)

            # handle the player actions
            if move == "D":
                # player is doubleing down, they can increase their bet
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print("Bet increased to {}.".format(bet))
                print("Bet:", bet)

            if move in ("H", "D"):
                # hit/doubling down takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print("You drew a {} of {}.".format(rank, suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    # the player has busted
                    continue

            if move in ("S", "D"):
                # stand/doubling down stops the player's turn
                break

        # handle the dealer's actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # the dealer hits:
                print("Dealer hits...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, True)

                if getHandValue(dealerHand) > 21:
                    break  # dealer has busted

                input("Press Enter to continue...")
                print("\n\n")

        # show the final hands
        displayHands(playerHand, dealerHand, True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        # handle whether the player won, lost or tied
        if dealerValue > 21:
            print("Dealer busts! You win ${}!".format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("You lost!")
            money -= bet
        elif playerValue > dealerValue:
            print("You won ${}!".format(bet))
            money += bet
        elif playerValue == dealerValue:
            print("It's a tie, the bet is returned to you.")

        input("Press Enter to continue...")
        print("\n\n")


def getBet(maxBet):
    """Ask the player how much they want to bet for this round.

    Args:
        maxBet (string): an amount the user wishes to bet
    """
    while True:  # keep asking until they enter a valid amount
        print("How much do you bet? (1 - {}, or QUIT)".format(maxBet))
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        if not bet.isdecimal():
            continue  # if the player didn't enter a number, ask again

        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  # player entered a valid bet


def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards."""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # add the numbered cards
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))  # add the face and ace cards
    random.shuffle(deck)
    return deck


def displayHands(playerHand, dealerHand, showDealerHand):
    """Show the player's and dealer's cards. Hide the dealer's first.

    Args:
        playerHand (string): string representing the player's hand
        dealerHand (string): string representing the dealer's hand
        showDealerHand (bool): if true, show the dealer's hand
    """
    print()
    if showDealerHand:
        print("DEALER:", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER: ???")
        # hide the dealer's first card
        displayCards([BACKSIDE] + dealerHand[1:])

    # show the player's cards:
    print("PLAYER:", getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    """Returns the value of the cards. Face cards are worth 10, aces are worth
    11 or 1 (this function picks the most suitable ace value).

    Args:
        cards (string[]): string array representing cards
    """
    value = 0
    numberOfAces = 0

    # add the value for the non-ace cards
    for card in cards:
        rank = card[0]  # card is a tuple like (rank, suit)
        if rank == "A":
            numberOfAces += 1
        elif rank in ("K", "Q", "J"):  # face cards are worth 10 points
            value += 10
        else:
            value += int(rank)  # Numbered cards are worth their number

    # add the value for the aces
    value += numberOfAces  # add 1 per ace

    for i in range(numberOfAces):
        # if another 10 can be added with busting, do so
        if value + 10 <= 21:
            value += 10

    return value


def displayCards(cards):
    """Display all the cards in the cards list.

    Args:
        cards (string[]): array of strings representing cards
    """
    rows = ["", "", "", "", ""]  # the text to display on each row

    for i, card in enumerate(cards):
        rows[0] += " ___  "  # print the top line of the card
        if card == BACKSIDE:
            # print a card's back
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "|_##| "
        else:
            # print the card's front
            rank, suit = card  # the card is a tuple data structure
            rows[1] += "|{} | ".format(rank.ljust(2))
            rows[2] += "| {} | ".format(suit)
            rows[3] += "|_{}| ".format(rank.rjust(2, "_"))

    # print each row on the screen
    for row in rows:
        print(row)


def getMove(playerHand, money):
    """Asks the player for their move, and returns "H" for hit, "S" for stand
    and "D" for double down.

    Args:
        playerHand (list): list of cards representing the player's hand
        money (int): amount of money the player has
    """
    while True:  # keep looping until the player enters a correct move
        # determine what moves the player can make
        moves = ["(H)it", "(S)tand"]
        # the player can double down on their first move, which we can tell
        # because they'll have exactly two cards
        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")
        # get the player's move
        movePrompt = ", ".join(moves) + "> "
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move  # player has entered a valid move
        if move == "D" and "(D)ouble down" in moves:
            return move  # player has entered a valid move


# if the program is run (instead of imported), run the game
if __name__ == "__main__":
    main()
