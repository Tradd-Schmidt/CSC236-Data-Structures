############################################################################################################
# Name: schmidtt-csc236A13
# Purpose: Produce all the mnemonics of a given phone number
#
# Author: Tradd Schmidt
# Using code adapted from Stack Overflow user Alex Martelli
# https://stackoverflow.com/questions/1851239/permutations-for-digits-represented-by-phone-number
#
############################################################################################################
import pip






def mnemonics(digs):
    """
    Takes a string of numbers and prints out every permutation of the phone number letter equivalents of each number in
    the order that the digits appear
    :param digs: The phone number that will be turned into words
    :return: a list of all the permutations of the string of numbers
    """
    phone = {"2": "abc", "3": "def",
             "4": "ghi", "5": "jkl", "6": "mno",
             "7": "pqrs", "8": "tuv", "9": "wxyz"}
    if len(digs) == 0:      # Base case for recursion
        yield ''
        return
    first, rest = digs[0], digs[1:]
    for x in phone[first]:
        for y in mnemonics(rest):
            yield x + y         # Combines the all of the letters except one tht is being altered


def main():
    valid = ["2", "3", "4", "5", "6", "7", "8", "9"]
    x = True
    while x:
        number = input("Please input a phone number with digits 2-9.")
        for i in number:
            if i in valid:
                x = False
            else:
                print("That sequence contained an invalid number.")
                x = True
                break
    print(mnemonics(number))

if __name__ == "__main__":
    main()
