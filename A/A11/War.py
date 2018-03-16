from Stack import Stack
from Queue import Queue


class War:
    def __init__(self):
        self.myCurrent = 0                # my currently displayed card
        self.otherCurrent = 0             # other currently displayed card
        self.currentState = True          # keeps track of the state of play
        self.dealingPile = Stack()        # stack
        self.myPlayingPile = Stack()      # stack
        self.myStoragePile = Queue()      # queue
        self.otherPlayingPile = Stack()   # stack
        self.otherStoragePile = Queue()   # queue
        self.lootPile = Stack()           # stack
        self.cards = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # a standard set of cards

    def add_dealingPile(self):
        """
        Adds cards to dealing pile
        :return: None
        """
        for i in range(5):
            for l in self.cards:
                self.dealingPile.push(l)
        self.dealingPile.shuffle()

    def deal(self):
        """
        Adds an equal amount of cards from the dealingPile to each players Playing Pile
        :return: None
        """
        while self.dealingPile.items != []:
            self.myPlayingPile.push(self.dealingPile.pop())
            self.otherPlayingPile.push(self.dealingPile.pop())

    def make_move(self):
        """
        initiates a round of play and communicates play-by-play during the round
        returns true when the game is still in play
        returns false when the game is over
        Communicates an appropriate message about whether the user beat the computer
        :return: a boolean
        """

        self.myCurrent = self.remove_my_card()
        self.otherCurrent = self.remove_other_card()
        print("You played a {0} card and the computer played a {1} card.".format(str(self.myCurrent),   # This is to state which 2 cards were played.
                                                                                 self.otherCurrent))
        self.lootPile.push(self.myCurrent)
        self.lootPile.push(self.otherCurrent)
        if self.compare_cards() == "equal":     # This enters the loop of War
            print("The cards were the same! THIS MEANS WAR!!!")
            while self.compare_cards() == "equal":
                self.myCurrent = self.remove_my_card()          # These are the cards that are discarded in war
                self.otherCurrent = self.remove_other_card()
                self.lootPile.push(self.myCurrent)
                self.lootPile.push(self.otherCurrent)
                self.myCurrent = self.remove_my_card()          # These are the cards that will be compared to try to win the war
                self.otherCurrent = self.remove_other_card()
                self.lootPile.push(self.myCurrent)
                self.lootPile.push(self.otherCurrent)
                if self.otherCurrent == "empty":        # These 2 statements are to make sure that neither side has run
                    break                               # out of cards this round of war
                elif self.myCurrent == "empty":
                    break
                print("You played a {0} card and the computer played a {1} card.".format(self.myCurrent,
                                                                                         self.otherCurrent))
                if self.compare_cards():            # Your card was higher
                    print("You have won the war!")
                    self.move_my_loot()
                elif not self.compare_cards():      # The computer's card was higher
                    print("You lost the war...")
                    self.move_other_loot()
        elif self.compare_cards():      # Your card was higher
            print("Your card was higher!")
            self.move_my_loot()
        elif not self.compare_cards():      # The computer's card was higher
            print("The computer's card was higher...")
            self.move_other_loot()
        if self.myPlayingPile.size() == 0:        # Checks if myPlayingPile is empty
            if self.myStoragePile.size() == 0:    # Checks if myStoragePile is empty, if it is, then the player loses
                print("You have run out of cards. You lose...")
                self.currentState = False
            else:
                self.move_my_storage()          # Refreshes the myPlayingPile
        if self.otherPlayingPile.size() == 0:       # Checks if otherPlayingPile is empty
            if self.otherStoragePile.size() == 0:   # Checks if otherStoragePile is empty, if it is, then the player wins
                print("The computer ran out of cards! You win!")
                self.currentState = False
            else:
                self.move_other_storage()       # Refreshes otherPlayingPile

    def remove_my_card(self):
        """
        Precondition: myPlayingPile is not empty
        If it is not empty, the function removes a card from myPlayingPile,
        returning the stored value
        :return: an integer
        """
        if self.myPlayingPile.size() == 0:
            if self.myStoragePile.size() == 0:
                return "empty"      # Used in the "war" section to check if a person has run out of cards
            else:
                self.move_my_storage()
                return self.myPlayingPile.pop()
        else:
            return self.myPlayingPile.pop()

    def remove_other_card(self):
        """
        Precondition: otherPlayingPile is not empty
        If it is not empty, the function removes a card from otherPlayingPile,
        returning the stored value
        :return: an integer
        """
        if self.otherPlayingPile.size() == 0:
            if self.otherStoragePile.size() == 0:
                return "empty"      # Used in the "war" section to check if a person has run out of cards
            else:
                self.move_other_storage()
                return self.otherPlayingPile.pop()
        else:
            return self.otherPlayingPile.pop()

    def display_card(self, pile):
        """
        Displays a card on the screen and returns the value
        :param pile: the pile from which the card will be pulled
        :return: an integer
        """
        try:
            try:
                print(str(pile.top()))
                return pile.top()
            except IndexError:
                self.move_my_storage()
                print(str(pile.top()))
                return pile.top()
        except AttributeError:
            try:
                print(str(pile.front()))
                return pile.front()
            except IndexError:
                self.move_other_storage()
                print(str(pile.front()))
                return pile.front()

    def compare_cards(self):
        """
        Compares myCurrent to otherCurrent and behaves appropriately
        :return: a boolean
        """
        if self.myCurrent > self.otherCurrent:      # Player's card was higher
            return True
        elif self.myCurrent < self.otherCurrent:    # Computer's card was higher
            return False
        elif self.myCurrent == self.otherCurrent:
            return "equal"          # The 2 cards were equal, so this is used to initiate war

    def move_my_loot(self):
        """
        Moves all cards from the loot pile to myStoragePile
        :return: None
        """
        while self.lootPile.size() > 0:
            self.myStoragePile.enqueue(self.lootPile.pop())

    def move_other_loot(self):
        """
        Moves all cards from the loot pile to otherStoragePile
        :return: None
        """
        while self.lootPile.size() > 0:
            self.otherStoragePile.enqueue(self.lootPile.pop())

    def move_my_storage(self):
        """
        Moves all cards from myStoragePile to myPlayingPile
        :return: None
        """
        while self.myStoragePile.size() > 0:
            self.myPlayingPile.push(self.myStoragePile.dequeue())
        self.myPlayingPile.shuffle()        # myPlayingPile is shuffled to keep it random

    def move_other_storage(self):
        """
        Moves all cards from otherStoragePile to otherPlayingPile
        :return: None
        """
        while self.otherStoragePile.size() > 0:
            self.otherPlayingPile.push(self.otherStoragePile.dequeue())
        self.otherPlayingPile.shuffle()     # Other PlayingPile is shuffled to keep it random
