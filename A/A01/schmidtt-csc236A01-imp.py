######################################################################
# Author: Tradd Schmidt
# Username: schmidtt
#
# Assignment: A01 implementation
#
# Purpose: To obtain a random integer to be used in selecting a body part to be added to a player's beetle.
#
######################################################################

import random   # This is needed later in the program to do our dice rolling

def get_body_part():
    """
    Will generate a random integer to simulate the rolling of a die and will return the corresponding body part to the
    resulting number
    Pre: none
    Post: an all lowercase string
    :return: an all lowercase string
    """

    l = ["body", "head", "legs", "eyes", "feelers", "tail"]  # This is a list that contains all the body parts that can be rolled for in order of 0-5
    x = random.randint(0, 5)    # This uses random to choose an integer 0-5 which will simulate the die roll
    if x == 2 or x == 3 or x == 4:
        print("A pair of " + l[x] + " were rolled.")
    else:
        print("A " + l[x] + " was rolled.")

    return l[x]     # This is to return whatever corresponding body part was received after the rolling of the die


def main():
    get_body_part()     # This is to check if my function was working correctly

main()
