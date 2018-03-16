# -------------------------------------------------------------------------------
# Name:        printDigit.py
# Purpose:  This program asks the user for a number
#        that is in base 10 and the new number base.
#        This program uses recursion to convert the
#        number, in which it keeps dividing the number
#        by the base until it reaches a number between
#        zero and the base, at which point it stops. It
#        outputs the digits during that process.
#
# Authors & roles:
#
# -------------------------------------------------------------------------------

# Put the definition of the printDigits() function after this line.


def printDigits(num, base):
    """
    precondition: base > 1
    :param num: an integer
    :param base: an integer
    :return: None
    """
    assert base > 1
    if num < base:
        print(str(num) + " ")
    else:
        printDigits(num // base, base)
        print(str(num % base) + " ")

# Put the driver function definition; i.e. main() after this line


def main():
    num = 0
    base = 0
    num = int(input("What is the number to convert: "))
    base = int(input("What is the new number base for that number: "))
    printDigits(num, base)

if __name__ == '__main__':
    main()
