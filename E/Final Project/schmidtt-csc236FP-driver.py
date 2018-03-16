# schmidtt-csc236FP-driver.py
# Tradd Schmidt 12/08/2017
#
# Purpose: Allow a user to play the game Trashcan from 1 - 10 rounds

# ----------------------------------------------------------------------

from Trashcan import Trashcan


def instructions():
    """
    Provides instructions on how to play Trashcan
    :return: None
    """
    print("Use enter to advance through the game.")
    input("")
    print("Each player will have a field they will need to try to clear that is initially filled with random cards.")
    input("")
    print("For a player to complete their field, they must continually draw cards to fill each slot with the"
          " appropriate card")
    print("When the correct card is placed in its appropriate spot, the card that was already there is picked up."
          " If that card's slot has not been filled yet, it is placed in that slot and the card that was there is your"
          " new card. This continues until you have a card whose slot has already been filled.")
    input("")
    print("Here is an example field: [7, 5, 4, 5, 2, 5, 9, 11, 10, 12]")
    print("You draw a 4. It is swapped with the card in the 4 spot.")
    print("[7, 9, 4, 'Four', 2, 5, 5, 11, 10, 12]")
    print("The four slot now says 'Four' to indicate that that slot has been filled with a 4.")
    print("The card that was there was a 5. The 5 card is now placed in the 5 slot.")
    print("[7, 5, 4, 'Four', 'Five', 5, 9, 11, 10, 12]")
    print("A 2 was in the 5 slot. The 2 is placed in the 2 slot.")
    print("[7, 'Two', 4, 'Four', 'Five', 5, 5, 11, 10, 12]")
    print("A 5 card was in the 2 slot. Since the 5 slot has been filled, nothing can be done.")
    input("")
    print("Cards that go into slots are 'Ace' up to '10'. If you draw a Jack or Queen, or if you draw a card whose slot"
          " has been filled, your turn ends.")
    print("If a King is drawn, you have the option of where to place it. If a card is drawn whose slot is filled with "
          "a King, the King is picked up, and it can placed in another slot.")
    input("")
    print("Each round that is completed, the number of slots on the field goes down for each player who cleared their "
          "field.")
    print("Whoever finishes the number of rounds first, wins.")
    input("")


def main():
    acceptable_rounds = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    new = input("Would you like instructions on how to play? (yes or no)")
    while True:
        if new == "yes":
            instructions()
            break
        elif new == "no":
            break
        else:
            print("I don't know what you mean.")
            new = input("Would you like instructions on how to play? (yes or no)")
    again = "yes"
    while again == "yes":
        rounds = input("How many rounds would you like to play? (1-10)")
        while rounds not in acceptable_rounds:
            print("That as an invalid input for rounds.")
            rounds = input("How many rounds would you like to play? (1-10)")

        game = Trashcan(int(rounds))
        check = True
        while check:
            check = game.play()
        again = input("Would you like to play again? (yes or no)")
        while True:
            if again == "yes" or again == "no":
                break
            else:
                print("I don't know what you mean.")
                again = input("Would you like to play again? (yes or no)")

    print("Thank you for playing.")


if __name__ == "__main__":
    main()
