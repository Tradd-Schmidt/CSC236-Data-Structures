################################################################################################
# Name: Toy
# Author: Tradd Schmidt
#
# Purpose: Creates a toy that can be played with by a Pet
#
################################################################################################


import time


class Toy:
    def __init__(self):
        self.battery_power = 70         # How much battery the toy has left

    def drain_battery(self, play_time):
        """
        This drains the battery_power based on how long the pet plays with the toy
        :param play_time: How long the toy was played with
        :return:
        """
        self.battery_power -= play_time

    def charge_battery(self):
        """
        This will charge the battery to max
        :return: none
        """
        time.sleep(35)
        self.battery_power = 70
