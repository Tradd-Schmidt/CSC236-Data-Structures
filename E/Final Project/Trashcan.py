from Queue import Queue
from Stack import Stack


class Trashcan:
    def __init__(self, rounds):
        self.rounds = rounds
        self.player_1_round = 10    # A counter to keep track of which round each person is on
        self.player_2_round = 10
        self.draw_pile = Stack()
        self.burn_pile = Stack()
        self.player_1_hand = Queue()
        self.player_2_hand = Queue()
        self.cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # Standard suit of cards
        self.cards_s = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.card_names = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]  # card name equivalents
        self.player_1_field = []
        self.player_2_field = []

    def create_draw_pile(self): # This code was reused from War.py
        """
        Adds cards to dealing pile
        :return: None
        """
        for i in range(4):
            for l in self.cards:
                self.draw_pile.push(l)
        self.draw_pile.shuffle()

    def draw(self, hand):
        """
        Takes a card from the top of the draw_pile and enqueues that card into the the provided player's hand
        :param hand: A queue for a player's cards held in their hand
        :return: None
        """
        card = self.draw_pile.pop()
        hand.enqueue(card)

    def create_playing_field(self, n, hand, field):  # This is the code I did BigO analysis for
        """
        Draws 10 cards to each player from the draw_pile. Then the playing fields get the cards from each players hand
        :return: None
        """
        while hand.size() < n:
            self.draw(hand)
        while hand.size() != 0:
            field.append(hand.dequeue())

    def placing_phase(self, hand, field, player_round):
        """
        Draws a card and places it in the appropriate spot. If a King is drawn, prompts the user to provide a slot to
        place it in. If a Jack or Queen is drawn, the cycle ends. If a drawn card can not be placed, the cycle ends.
        :param hand: The hand of the current player
        :param field: The field of the current player
        :param player_round: what round the player is on
        :return: None
        """
        if self.draw_pile.size() == 0:  # If the draw pile is empty, it is refreshed using the burn pile
            self.refresh()
        self.draw(hand)
        while True:
            card = hand.dequeue()
            if card == 0 or card == 7:      # Code to print out what was drawn using an if the card is an Ace or 8
               input("An " + self.card_names[card] + " was drawn.")
            else:                           # Code to print out what was drawn for all other cards
               input("A " + self.card_names[card] + " was drawn.")
            if player_round <= card < 12:    # If the card is a Jack or Queen
                print("Nothing could be done. . .")
                break
            elif card == 12 or card == "King":      # If the card is a King
                print("Here is your current field:")    # Just a reminder to the player of what they have so far.
                print(field)
                choice = input("Choose a number between 1 and 10 to place the king in that spot.")  # Asks where the user wants the King
                while True:
                    while choice not in self.cards_s:
                        print("That was an invalid choice.")
                        choice = input("Choose a number between 1 and 10 to place the king in that spot")
                    choice = int(choice)
                    if isinstance(field[choice - 1], str):  # Checks to see if the slot has been filled by checking if the type is a string
                        choice = input("That spot has already been filled with the correct card. Please provide "
                                       "another number")
                    else:
                        hand.enqueue(field[choice - 1])     # Fills the slot with a King
                        field[choice - 1] = "King"
                        break
            elif field[card] == "King":     # Checks to see if the slot has a King so the King can be reused
                hand.enqueue(12)
                field[card] = self.card_names[card]
                print("   " + str(field))
                input("")
            elif not isinstance(field[card], str):      # If it is not a King, this checks if the slot can be filled with the card
                hand.enqueue(field[card])
                field[card] = self.card_names[card]
                print("   " + str(field))
                input("")
            else:     # If nothing else can be done, the card in the hand is put in the burn pile and the cycle ends
                print("Nothing could be done. . .")
                self.burn_pile.push(card)
                break

    def check_field(self, field):
        """
        Checks a field to see if it is been completed.
        :param field: field to be checked
        :return: A boolean
        """
        for i in field:
            if not isinstance(i, str):
                return True
        return False

    def reset(self):
        """
        Clears all of the hands, piles, and fields.
        :return: None
        """
        del self.player_1_field[:]
        del self.player_2_field[:]
        self.draw_pile.clear()
        self.burn_pile.clear()
        self.player_1_hand.clear()
        self.player_2_hand.clear()

    def refresh(self):
        """
        Moves all cards from the burn pile to the draw pile
        :return: None
        """
        for i in range(self.burn_pile.size()):
            self.draw_pile.push(self.burn_pile.pop())
        self.draw_pile.shuffle()

    def end_of_round(self):
        """
        Prints out the progress of each player and calls reset() to end the round.
        :return: None
        """
        print("Player 1 has " + str(self.player_1_round) + " cards to fill and Player 2 has " +str(self.player_2_round)
              + " cards to fill.")
        self.reset()

    def play(self):
        """
        Creates the drawing pile, the fields, and goes through the placing phase until a player completes their field.
        Whichever players completed their field move on to the next round with 1 less slot to fill.
        :return: A Boolean
        """
        self.create_draw_pile()
        self.create_playing_field(self.player_1_round, self.player_1_hand, self.player_1_field)
        self.create_playing_field(self.player_2_round, self.player_2_hand, self.player_2_field)
        while True:
            input("Player 1's turn. Press enter to start.")
            self.placing_phase(self.player_1_hand, self.player_1_field, self.player_1_round)
            input("Player 2's turn. Press enter to start.")
            self.placing_phase(self.player_2_hand, self.player_2_field, self.player_2_round)

            if not self.check_field(self.player_1_field) and not self.check_field(self.player_2_field):  # Checks if both players finished
                self.player_1_round -= 1
                self.player_2_round -= 1
                break
            elif not self.check_field(self.player_1_field):  # If both players didn't finish, checks if Player 1 finished
                self.player_1_round -= 1
                break
            elif not self.check_field(self.player_2_field):  # Checks if Player 2
                self.player_2_round -= 1
                break
        if self.player_1_round == 10 - self.rounds:  # Checks if player 1 has won
            print("Player 1 has won!")
            return False
        elif self.player_2_round == 10 - self.rounds:  # Checks if player 2 has won
            print("Player 2 has won!")
            return False
        else:   # If neither player has won yet, this ends the round
            self.end_of_round()
            return True
