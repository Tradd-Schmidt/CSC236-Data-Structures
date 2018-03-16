# -------------------------------------------------------------------------------
# Name:     LinkedList_smdriver.py
# Purpose:  Rudimentary driver for the LinkedList class.
#
# Edited by: Tradd Schmidt on 9/21/17
# -------------------------------------------------------------------------------

from LList import LList


def main():
    print("Make a linked list in honor of Donna Schmidt")
    mom = LList((8, 21, 1962))  # Named after Donna Schmidt, my mom because she is the strongest willed person I know
    print("Make a linked list in honor of Jim Carrey")
    truman = LList((6, 17, 1962))  # Named after Jim Carrey because he is always his true with himself and others about who he is
    print("Make a linked list for a fictional character")
    fictional = LList(((8 + 6) // 2, (21 + 17) // 2, 1962))    # Fictional persons birthday

    # Printing the Birthdays
    # ---------------------------------------------------------------------------------------
    print("\n")
    print("Printing Donna's birthday")
    for item in mom:
        print(str(item) + " ",)
    print("\n")
    print("Printing Jim Carrey's birthday")
    for item in truman:
        print(str(item) + " ",)
    print("\n")
    print("Printing the fictional character's birthday")
    for item in fictional:
        print(str(item) + " ",)

    # Changing the year of the fictional character
    # ---------------------------------------------------------------------------------------
    year = fictional._find(len(fictional) - 1)
    year.item += 100
    print("\n")
    print("Printing the fictional character's revised birthday")
    for item in fictional:
        print(str(item) + " ", )

    # Deleting the date of the fictional character's birthday
    # ----------------------------------------------------------------------------------------
    fictional.__delitem__(1)
    print("\n")
    print("Printing the fictional character's revised birthday")
    for item in fictional:
        print(str(item) + " ", )


main()
