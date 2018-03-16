######################################################################
# Author: Dr. Jan Pearce  ****** CHANGE THIS!! ******
# username: pearcej ****** CHANGE THIS!! *****

# Assignment: A15
# Purpose: To learn more about lists of lists and deep copies and also
# to enhance a larger module (ppm.py)
######################################################################
# Acknowledgements:
    # Ben Stephenson: http://pages.cpsc.ucalgary.ca/~jacobs/Courses/cpsc217/W10/code/Topic7/ppm.py
    # working from a class: http://bytes.com/topic/python/answers/520360-trouble-displaying-image-tkinter

# You need to acknowledge having modified this code and all other code you modify or use for assistance.
#   To do so, you will indicate something like:
#   Modified from code written by Dr. Jan Pearce
#   Modified by Mario Nakazawa, convert to run in Python 3.X. Commented references to tkinter which broke.
#   Original code downloaded from:
#   http://cs.berea.edu/csc226/tasks/yourusername-L3-ppm.py and
#   http://cs.berea.edu/csc226/tasks/ppm.py
######################################################################

import time
from ppm_schmidtt import *
# Be sure you work with a single ppm object at a time


def read_words(words_file_name):
    '''This function opens a file with the name in 'words_file', reads in
    the contents and returns a list of the words, stripped of whitespace.
    pre: none, as this function handles IOError for when the file is not there gracefully
    post: returns the list of words in the file, which is empty on an open fail. '''
    words_list =[]
    try:
        open_file = open(words_file_name, 'r')
        contents = open_file.readlines()

        for i in range(len(contents)):
            words_list.extend((contents[i].split()))
        open_file.close()
    except IOError:
        print("File does not exist! Try again.")
    return words_list


def main():
    # The following interaction is just for testing.  You will improve this.

    wn = PPM_set_up()  # To use the PPM class, this must appear at the beginning of your program: send to the initialzer.

    print("\nWelcome to the PPM introduction!\n")
    text = input("Please input name of PPM-P3 file: ")
    # ppmdefault = PPM(wn) # uses default file
    # ppmdefault.PPM_display()
    # print("---")
    text = read_words(text)
    filename = input("Please input name of PPM-P3 file: ")
    reference = filename
    ppmobject = PPM(wn, filename)
    referenceppm = PPM(wn, reference)
    # ppmobject.PPM_make_red()
    ppmobject.PPM_embed_text(text)
    ppmobject.PPM_extract_text(referenceppm.pixellist)
    ppmobject.PPM_display()

    # print("---")

    # ppmtestlist = PPM(wn) # uses default file
    # ppmtestlist.outasciifile = "very_small_asc.ppm"
    # ppmtestlist.outbinfile = "very_small_bin.ppm"
    # The following is a very small image list which differs from the default image
    # testlist = [[[0, 0, 255], [0, 255, 0], [0, 30, 30]],
    #             [[40, 40, 40], [50, 50, 50],[60, 60, 60]]]
    # ppmtestlist.PPM_updatefrompixellist(testlist, "very_small.ppm")
    # ppmtestlist.PPM_display()

    print("\nPush the Quit button to exit all files.")

    PPM_render(wn)  # needed to render all of the images you have instantiated

main()
