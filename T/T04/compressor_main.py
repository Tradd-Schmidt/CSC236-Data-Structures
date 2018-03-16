#-------------------------------------------------------------------------------
# Name:        compressor_main.py
# Purpose:  The main() function exists in this file for the program that uses
#   the Compresser and Hopper classes in the compressor.py and hopper.py files
#   in the same directory.
#
# Created:     31/08/2014
#-------------------------------------------------------------------------------

from compressor import Compresser
from hopper import Hopper

def main():
    theCompressor = Compresser()    # create a Compressor object
    theHopper = Hopper()            # create a Hopper object
    theHopper.fill_coal()           # fill out the Hopper object with coal

    # loop through and have the Compressor object take coal out of the Hopper
    # and compress it.
    for i in range(10):
        print(theHopper)
        theCompressor.get_coal(theHopper)
        theCompressor.compress()
    print(theCompressor)

if __name__ == '__main__':
    main()
