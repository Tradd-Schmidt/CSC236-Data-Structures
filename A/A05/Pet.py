###########################################################################################
# Name: Pet
# Author: Tradd Schmidt
#
# Purpose: Create a pet than can play with a toy
#
###########################################################################################


import time


class Pet:
    def __init__(self):
        self.happiness = 100        # If this falls to 0 or below, the pet dies
        self.energy = 60            # How much energy the pet has to play with the toy
        self.alive = True           # Checks to see if the pet is still alive

    def play_with_toy(self, play_time):
        """
        Allows the pet to play with the toy and increase the happiness level.
        :param play_time: How long the toy is played with
        :return: none
        """
        if play_time >= 100:                # If the happiness would be increased by more than 100 which is the max
            self.happiness = 100            # the happiness is just set to 100
            self.energy -= play_time
        else:                               # Otherwise, current happiness is increased by the amount of time the toy
            self.happiness += play_time     # played with
            self.energy -= play_time

    def sleep(self):
        time.sleep(60)
        self.energy = 60

    def idle(self):
        if self.happiness <= 0:             # Kills the pet if it is idle too long
            self.alive = False
