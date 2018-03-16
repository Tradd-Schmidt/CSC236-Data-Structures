# -------------------------------------------------------------------------------
# Name:        count_evens.py
# Purpose:  This program is designed to use recursion to count the number of
#           even numbers are read from a file. This sequence is stored in a
#           linked list.
#
# Created:     08/10/2014
# -------------------------------------------------------------------------------

from ListNode import ListNode
from LList import LList

# recursive function to count the number of even numbers in this linked list.


def count_evens(currentNode, maximum):
    """
    Keeps track of the largest item of the linked list and returns it
    :param currentNode: Current node being checked
    :param maximum: The maximum value so far
    :return: the maximum value
    """
    if currentNode == None:
        return maximum
    else:
        if currentNode.item > maximum:
            maximum = currentNode.item
            return count_evens( currentNode.link, maximum)
        else:
            return count_evens(currentNode.link, maximum)


def read_numbers_return_list( ):
    '''preconditions: none
    postconditions: the numbers in the file with the name asked by the user will
        be placed into a linked list and returned.'''
    filename = input("What is the name of the file?")

    file = open(filename, "r")

    # get the list of strings from the file. This list will need to be converted to
    # a list of numbers in a
    stringList = file.read().split()
    file.close()

    # time to create an integer version of the numbers list
    numberList = []
    for item in stringList :
        numberList.append(int(item))

    # Now create a linked list version of this number sequence
    created_list = LList(numberList)
    return created_list


def main():

    numbersList = read_numbers_return_list()
    print( count_evens( numbersList.head, numbersList.head.item) )

if __name__ == '__main__':
    main()
