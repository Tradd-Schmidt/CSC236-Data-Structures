######################################################################
# Author: Tradd Schmidt
# Username: Schmidtt
#
# Assignment: A11: PPM
#
# Purpose:  A module for loading and displaying PPM-P3 files using Python
######################################################################
# Usage Instructions:
#
# To use you must call a helper function:
# wn = PPM_set_up()
#
# Following this, you may use the class methods which reads an input PPM-P3 file in the constructor.
# It never writes to the input file, instead creating two output files with
# "-asc" and "-bin", respectively appended to the input filename.
# These are intended for the user's use and to display respectively.
#
# to render the image:
# PPM_render(wn)   # needed to render all of the images you have instantiated where the argument is that which
#                  # was returned from PPM_set_up()
#
# The image data is stored in the following member variables:
# self.magic
# self.width
# self.height
# self.colormax
# self.pixellist
#
# # Constructor usage examples:
# df = PPM()
# df = PPM("bc-flowers.ppm")
#
#
# Display image example:
# df.PPM_display()
#
#
# Change image by changing pixellist:
# bc.PPM_updatefrompixellist(mylist)
#
######################################################################
# Acknowledgements:
#
# Original code written by Dr. Jan Pearce, Berea College
#
# Attributions:
    # Ben Stephenson: http://pages.cpsc.ucalgary.ca/~jacobs/Courses/cpsc217/W10/code/Topic7/ppm.py
    # working from a class: http://bytes.com/topic/python/answers/520360-trouble-displaying-image-tkinter
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import tkinter as tk    # for display of the PPM image
import copy             # You might need this later...

####################
# This section represents helper functions which are needed by the PPM class.
global tkintertoggle        # Needed as global to ensure a single Tkinter instance
tkintertoggle = False


def PPM_set_up(): # This must be called at the beginning of any program which uses the PPM class
    """
    Sets up the Tkinter root instance which allows for image windows

    :return: a Tk tkinter object
    """
    master = tk.Tk()
    return master           # save and send to all PPM methods which need it, including the initializer


def PPM_render(master):
    """
    Renders all PPM instances

    :param master: a Tk tkinter object
    :return: None
    """
    master.mainloop()
# End helper functions section
####################


class PPM_Exception(Exception):
    """
    Create a Python class to enable meaningful error messages on exceptions.
    """
    def __init__(self, value):
        """
        Initializer method for the PPM_Exception class.

        :param value: the exception value
        """
        self.value = value

    def __str__(self):
        """
        Modifies the str method to return more meaningful error messages
        :return: a string representing the error message
        """
        return repr(self.value) # allows a meaningful error message to be displayed

# End PPM_Exception class


class PPM:
    """
    Class which can be used to open, close, and display PPM P3 (ASCII) files.
    """

    PPMDEFAULT = '''P3
# Created by OOM class, by Dr. Jan Pearce, Berea College
8 10
255
140 140 140 120 120 120 100 100 100 80 80 80 60 60 60 40 40 40 20 20 20 0 0 0
120 120 120 63 72 204 63 72 204 63 72 204 63 72 204 252 252 255 255 255 255 15 15 15
105 105 105 255 255 255 63 72 204 255 255 255 63 72 204 255 255 255 255 255 255 30 30 30
90 90 90 255 255 255 63 72 204 63 72 204 63 72 204 255 255 255 255 255 255 45 45 45
75 75 75 255 255 255 63 72 204 255 255 255 63 72 204 63 72 204 63 72 204 60 60 60
60 60 60 63 72 204 63 72 204 63 72 204 63 72 204 255 255 255 63 72 204 75 75 75
45 45 45 255 255 255 255 255 255 63 72 204 255 255 255 254 254 254 255 255 255 90 90 90
30 30 30 255 255 255 255 255 255 63 72 204 255 255 255 255 255 255 63 72 204 105 105 105
15 15 15 252 252 253 255 255 255 63 72 204 63 72 204 63 72 204 63 72 204 120 120 120
0 0 0 20 20 20 40 40 40 60 60 60 80 80 80 100 100 100 120 120 120 140 140 140'''
    def __init__(self, master, inasciifile = "default.ppm"):
        """
        Opens or creates a PPM P3 file named inasciifile to construct a PPM object

        :param master: a Tk tkinter object
        :param inasciifile: the input ascii file representing the image
        """
        global tkintertoggle            # This must be global to allow multiple PPM objects but make only a single Quit button on the Tkinter canvas.
        self.root = master
        self.root.title("PPM Quit")

        if tkintertoggle == False:
            tk.Button(self.root, text="QUIT", fg="red", command=self.root.quit).pack()
            tkintertoggle = True

        if inasciifile == "": # makes default.ppm as input file if none exists
            inasciifile = "default.ppm"

        self.inasciifile = inasciifile                  # This file is used only for reading
        self.outasciifile = inasciifile[:-4]+"-asc.ppm" # created to store modifications
        self.outbinfile = inasciifile[:-4]+"-bin.ppm"   # binary ppm filename needed for viewing
        self.title = inasciifile                        # used for the title of the display window
        self.magic = "P3"                               # ppm file type
        self.comment = "# Created by ppm-class, by Dr. Jan Pearce\n"
        self.width = 0
        self.height = 0
        self.colormax = 255         # should be set to 255
        self.ascii = ""             # will store the color intensities in P3 format
        self.pixellist = []         # will store nested list containing pixel colors
        self.image = ""             # It is necessary that this be a member variable for Tk to display image correctly
        # If there is no filename given, make a file to work with
        self.label = ""             # Used to place image in window
        if self.inasciifile == "default.ppm" :
            self.ascii = self.PPMDEFAULT
            tmpfile = open(self.inasciifile, "w")
            tmpfile.write(self.ascii)
            tmpfile.close()
        print("PPM object created from {0}".format(self.inasciifile))
        self.PPM_makeoutputfiles()  # Makes ascii and binary output files

    def PPM_makeoutputfiles(self):
        """
        Given self.inasciifile, sets self.ascii and creates both ascii and binary files for output

        :return: None
        """
        outtmpfile = open(self.outasciifile, "w")
        intempfile = open(self.inasciifile, 'r')        # self.inasciifile must have data
        self.ascii = intempfile.read()
        outtmpfile.write(self.ascii)
        intempfile.close()
        outtmpfile.close()
        self.PPM_load(self.inasciifile)
        self.PPM_convert2bin()

    def PPM_partition(self, strng, ch):
        """
        Returns a triple with all characters before the delimiter, the delimiter itself if present,
        and all of the characters after the delimiter (if any)

        :param strng: a string to partition
        :param ch: the character to use as the delimiter
        :return: a tuple containing 1) the string, 2) the delimiter, and 3) all characters after the delimiter
        """
        if ch in strng:
            i = strng.index(ch)
            return (strng[0:i], strng[i], strng[i+1:])
        else:
            return (strng, None, None)

    def PPM_clean(self, strng):
        """
        Removes all single line comments present in a string, including all white space at the end,
        the newline, and linefeed characters.

        :param strng: an input string
        :return: A string with all characters after the comment character removed.
        """
        (retval, junk1, junk2) = self.PPM_partition(strng, "#")
        return retval.rstrip(" \t\n\r")

    def PPM_load(self, inasciifile):
        """
        Input parameter inasciifile is a string containing the name of the file to load
        Assumes an ASCII PPM-P3 (non-binary) file.
        Loads the named image file from disk, and stores the image data in member variables.

        :param inasciifile: the name of the file to load
        :return: None
        """

        # Open the input file
        infile = open(self.inasciifile,"r")

        # Read the magic number out of the top of the file and verify that we are
        # reading from an ASCII PPM-P3 file
        tmpln = infile.readline()
        self.ascii += tmpln
        self.magic = self.PPM_clean(tmpln)
        if (self.magic != "P3"):
            raise PPM_Exception('The file being loaded does not appear to be a valid ASCII PPM-P3 file')

        # Get the image dimensions
        tmpln = infile.readline()
        while tmpln[0] == '#':          # Dump full comment lines
            tmpln = infile.readline()
        self.ascii += tmpln
        imgdimensions = self.PPM_clean(tmpln)

        # Unpack dimensions
        (width, sep, height) = self.PPM_partition(imgdimensions," ")
        self.width = int(width)
        self.height = int(height)
        if (self.width <= 0) or (self.height <= 0):
            raise PPM_Exception("The file being loaded does not appear to have valid dimensions ({0} x {1})".format(str(width), str(height)))

        # Get the maximum color value, which is assumed to be 255
        tmpln = infile.readline()
        self.ascii += tmpln
        self.colormax = int(self.PPM_clean(tmpln))
        if (self.colormax != 255):
            raise PPM_Exception("Warning: PPM file does not have a maximum intensity value of 255.  Image may not be handled correctly.")

      # Create a list of the color intensities
        color_list = []                     # hold intensity data temporarily in a list of intensity strings
        for line in infile:
            self.ascii += line
            line = self.PPM_clean(line)
            color_list += line.split(" ")
        infile.close()                      # Close input file since done
        self.PPM_makepixellist(color_list)  # Creates self.pixellist, a nested list of rows of [red, green, blue] pixels

    def PPM_makepixellist(self, color_list):
        """
        Creates self.pixellist, a nested list of rows of [red, green, blue] pixels
        from a color_list which contains an unnested list of strings

        :param color_list: a list of strings representing the colors
        :return: None
        """
        rcount = 0
        gcount = 1
        bcount = 2
        self.pixellist = []
        for row in range(self.height):
            self.pixellist.append([])
            for col in range(self.width):
                self.pixellist[row].append([int(color_list[rcount]), int(color_list[gcount]), int(color_list[bcount])])
                rcount += 3     # move to next red
                gcount += 3     # move to next green
                bcount += 3     # move to next blue

    def PPM_updatefrompixellist(self, pixellist, title="from_pixellist"):
        """
        Updates image object data and related files from input pixellist

        :param pixellist: a list of pixels
        :param title: the title of the window
        :return: None
        """
        strout = ""
        self.magic = "P3"
        self.colormax = 255
        self.width = len(pixellist[0])
        self.height = len(pixellist)
        header = self.magic+"\n"
        header += self.comment
        header += str(self.width) + " " + str(self.height)+"\n"+str(self.colormax)+"\n" # header is in ASCII
        for rowlist in pixellist:
            for pixel in rowlist:
                for color in pixel:
                    strout += str(color)+" "
            strout += "\n"
        self.ascii = header + strout
        self.pixellist = pixellist
        tmpfile = open(self.outasciifile, "w")
        tmpfile.write(self.ascii)
        tmpfile.close() #close tmpfile when done
        print("PPM object changed based upon list.")
        if self.title == "default.ppm":
            self.title = title
        self.PPM_convert2bin()

    def PPM_convert2bin(self):
        """
        Converts PPM-P3 to PPM-P6 using self.pixellist

        [04/07/2017] Credit to Conner Bondurant for fixing this function to work correctly Python 3

        :return: None
        """
        header = "P6\n"
        header += self.comment
        header += str(self.width) + " " + str(self.height)+"\n" + "255\n" # header is in ASCII
        strout = bytes()

        for rowlist in self.pixellist:
            for pixel in rowlist:
                for color in pixel:
                    strout += color.to_bytes(1, byteorder='big')

        # First write the header as ascii
        tmpfile = open(self.outbinfile, "w", newline="\n")
        tmpfile.write(header)
        tmpfile.close()         #close tmpfile when done
        # Then, write the image as binary
        tmpfile = open(self.outbinfile, "ab")
        tmpfile.write(strout)
        tmpfile.close()         #close tmpfile when done

    def PPM_set_title(self, title):
        """
        Setter for self.title (title of display window.)

        :param title: The title of the display window
        :return: None
        """
        self.title = title

    def PPM_display(self):
        """
        Displays PPM-P3 binary file using Tkinter

        :return: None
        """
        self.mywindow = tk.Toplevel(self.root)
        self.mywindow.geometry(str(self.width) + "x" + str(self.height)) # sets correct window size
        self.mywindow.wm_title(self.title)
        self.image = tk.PhotoImage(file = self.outbinfile)
        self.label = tk.Label(self.mywindow, image = self.image)
        self.label.place(x = 0, y = 0, height = self.height, width = self.width)

    def PPM_make_red(self):
        """
        Colorizes current image to red by using self.pixellist

        :return: None
        """
        newpixellist = self.pixellist
        self.width = len(newpixellist[0])
        self.height = len(newpixellist)
        row = 0
        for rowlist in newpixellist:
            col = 0
            for pixel in rowlist:
                newpixellist[row][col][1] = 0 # update green
                newpixellist[row][col][2] = 0 # update blue
                col += 1
            row += 1
        print(self.outasciifile + " output file turned red.")
        self.PPM_updatefrompixellist(newpixellist)      # This call will update all member attributes appropriately.

    def PPM_grayscale(self):
        """
        Converts image to grayscale

        :return: None
        """
        # Hint: What needs to be done here is to convert newpixellist to the equivalent greyscale image.
        # The final call to self.PPM_updatefrompixellist(newpixellist) is essential for updating member attribute appropriately.

        newpixellist = self.pixellist
        self.width = len(newpixellist[0])
        self.height = len(newpixellist)
        row = 0
        for rowlist in newpixellist:
            col = 0
            for pixel in rowlist:
                gray = (newpixellist[row][col][0]+newpixellist[row][col][1]+newpixellist[row][col][2])//3
                newpixellist[row][col][0] = gray
                newpixellist[row][col][1] = gray
                newpixellist[row][col][2] = gray
                col += 1
            row += 1
        print(self.outasciifile + " output file turned gray.")

        self.PPM_updatefrompixellist(newpixellist)      # This call will update all member attributes appropriately.

    def PPM_flip_horizontal(self):
        """
        Flips image horizontally

        :return: None
        """
        newpixellist = self.pixellist
        newpixellist2 = copy.deepcopy(newpixellist)
        self.width = len(newpixellist[0])
        self.height = len(newpixellist)
        row = 0
        for rowlist in newpixellist:
            col = 0
            col2 = 0
            for pixel in rowlist:
                newpixellist2[row][col2] = newpixellist[row][col-1]
                col -= 1
                col2 += 1
            row += 1
        newpixellist = newpixellist2
        print(self.outasciifile + " output file flipped horizontally.")
        # Hint 1: What needs to be done here is to convert newpixellist to the equivalent horizontally flipped image.
        # Hint 2: You might want a new object of the correct size or a deep copy.
        # The final call to self.PPM_updatefrompixellist(newpixellist) is essential for updating member attribute appropriately.


        self.PPM_updatefrompixellist(newpixellist) # This call will update all member apttributes appropriately.

    def PPM_rotateclockwise(self):              # Couldn't figure this one out
        """
        Rotates image clockwise

        :return: None
        """
        for i in range(3):
            newpixellist = self.pixellist
            self.width = len(newpixellist[0])
            self.height = len(newpixellist)
            row = 0
            transposed = [[row[i] for row in newpixellist] for i in range(self.height)]
            self.height = len(newpixellist[0])
            self.width = len(newpixellist)
            for rowlist in transposed:
                col = 0
                new_x = 0
                for pixel in rowlist:
                    new_y = abs(len(transposed[0]) - 1 - row)
                    transposed[row][col] = newpixellist[new_x][new_y]
                    col += 1
                    new_x += 1
                row += 1
            self.pixellist = transposed

        # Hint 1: What needs to be done here is to convert newpixellist to the equivalent rotated image.
        # Hint 2: It might be helpful to make a new object of the correct size
        # The final call to self.PPM_updatefrompixellist(newpixellist) is essential for updating member attribute appropriately.


        self.PPM_updatefrompixellist(transposed) # This call will update all member attributes appropriately.

    def PPM_make_green(self):
        newpixellist = self.pixellist
        self.width = len(newpixellist[0])
        self.height = len(newpixellist)
        row = 0
        for rowlist in newpixellist:
            col = 0
            for pixel in rowlist:
                newpixellist[row][col][0] = 0
                newpixellist[row][col][2] = 0
                col += 1
            row += 1
        print(self.outasciifile + " output file turned green.")

        self.PPM_updatefrompixellist(newpixellist)

    def PPM_make_blue(self):
        newpixellist = self.pixellist
        self.width = len(newpixellist[0])
        self.height = len(newpixellist)
        row = 0
        for rowlist in newpixellist:
            col = 0
            for pixel in rowlist:
                newpixellist[row][col][0] = 0
                newpixellist[row][col][1] = 0
                col += 1
            row += 1
        print(self.outasciifile + " output file turned blue.")

        self.PPM_updatefrompixellist(newpixellist)

    def PPM_sepia(self):
        newpixellist = self.pixellist
        self.width = len(newpixellist[0])
        self.height = len(newpixellist)
        row = 0
        for rowlist in newpixellist:
            col = 0
            for pixel in rowlist:
                r = newpixellist[row][col][0]
                g = newpixellist[row][col][1]
                b = newpixellist[row][col][2]
                sr = int(0.393*r + 0.769*g + 0.189*b)
                sg = int(0.349*r + 0.686*g + 0.168*b)
                sb = int(0.272*r + 0.534*g + 0.131*b)
                if sr > 255:
                    newpixellist[row][col][0] = 255
                else:
                    newpixellist[row][col][0] = sr
                if sg > 255:
                    newpixellist[row][col][1] = 255
                else:
                    newpixellist[row][col][1] = sg
                if sb > 255:
                    newpixellist[row][col][2] = 255
                else:
                    newpixellist[row][col][2] = sb
                col += 1
            row += 1
        print(self.outasciifile + " output file turned sepia.")

        self.PPM_updatefrompixellist(newpixellist)

    def letter_to_bin(self, letter):
        """
        Gives the binary of a given letter
        :param letter: A single string character
        :return: an integer
        """
        bin_dict = {" ": 32, "!": 33, '"': 34, "#": 35, "$": 36, "%": 37,
                    "&": 38, "'": 39, "(": 40, ")": 41, "*": 42, "+": 43,
                    ",": 44, "-": 45, ".": 46, "/": 47, "0": 48, "1": 49,
                    "2": 50, "3": 51, "4": 52, "5": 53, "6": 54, "7": 55,
                    "8": 56, "9": 57, ":": 58, ";": 59, "<": 59, "=": 60,
                    ">": 61, "?": 62, "@": 63, "A": 64, "B": 65, "C": 66,
                    "D": 67, "E": 68, "F": 69, "G": 70, "H": 71, "I": 72,
                    "J": 73, "K": 74, "L": 75, "M": 76, "N": 77, "O": 78,
                    "P": 79, "Q": 80, "R": 81, "S": 82, "T": 83, "U": 84,
                    "V": 85, "W": 86, "X": 87, "Y": 88, "Z": 89, "[": 90,
                    "\\": 91, "]": 92, "^": 93, "_": 94, "`": 95, "a": 96,
                    "b": 97, "c": 98, "d": 99, "e": 100, "f": 101, "g": 102,
                    "h": 103, "i": 104, "j": 105, "k": 106, "l": 107, "m": 108,
                    "n": 109, "o": 110, "p": 111, "q": 112, "r": 113, "s": 114,
                    "t": 115, "u": 116, "v": 117, "w": 118, "x": 119, "y": 120,
                    "z": 121, "{": 123, "|": 124, "}": 125, "~": 126, "DEL": 127}
        if letter in bin_dict:
            return bin_dict[letter]

    def bin_to_letter(self, number):
        """
        Takes an integer and converts it into a character and that character is returned
        :param number: an integer that corresponds to a character
        :return: a string
        """
        num_dict = {32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%',
                    38: '&', 39: "'", 40: '(', 41: ')', 42: '*', 43: '+',
                    44: ',', 45: '-', 46: '.', 47: '/', 48: '0', 49: '1',
                    50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7',
                    56: '8', 57: '9', 58: ':', 59: '<', 60: '=', 61: '>',
                    62: '?', 63: '@', 64: 'A', 65: 'B', 66: 'C', 67: 'D',
                    68: 'E', 69: 'F', 70: 'G', 71: 'H', 72: 'I', 73: 'J',
                    74: 'K', 75: 'L', 76: 'M', 77: 'N', 78: 'O', 79: 'P',
                    80: 'Q', 81: 'R', 82: 'S', 83: 'T', 84: 'U', 85: 'V',
                    86: 'W', 87: 'X', 88: 'Y', 89: 'Z', 90: '[', 91: '\\',
                    92: ']', 93: '^', 94: '_', 95: '`', 96: 'a', 97: 'b',
                    98: 'c', 99: 'd', 100: 'e', 101: 'f', 102: 'g', 103: 'h',
                    104: 'i', 105: 'j', 106: 'k', 107: 'l', 108: 'm', 109: 'n',
                    110: 'o', 111: 'p', 112: 'q', 113: 'r', 114: 's', 115: 't',
                    116: 'u', 117: 'v', 118: 'w', 119: 'x', 120: 'y', 121: 'z',
                    123: '{', 124: '|', 125: '}', 126: '~', 127: 'DEL'}
        if number in num_dict:
            return num_dict[number]

    def extract_letters(self, list_of_words):
        """
        Iterates through individual elements of a list to yield individual letters
        :param list_of_words: A list where each element is a word
        :return:
        """
        l = []
        for i in list_of_words:
            for q in i:
                l.append(self.letter_to_bin(q))
        return l

    def PPM_embed_text(self, text):
        """
        Takes a list of words and embeds the words into the ppm image
        :param text: A list of words
        :return: None
        """
        newpixellist = self.pixellist
        self.width = len(newpixellist[0])
        self.height = len(newpixellist)
        l = self.extract_letters(text)
        count = 0
        limit = len(l)
        row = 0
        for rowlist in newpixellist:
            if count >= limit:
                break
            col = 0
            for pixel in rowlist:
                newpixellist[row][col][2] = l[count]
                count += 1
                col += 1
                if count >= limit:
                    break
            row += 1
        print(self.outasciifile + " output file has been embedded with text.")

        self.PPM_updatefrompixellist(newpixellist)  # This call will update all member attributes appropriately.
        return l

    def PPM_extract_text(self, reference):
        """
        Compares the values of two pixel lists and extracts the text that has been embedded
        :param reference: Reference pixel list
        :return:
        """
        newpixellist = self.pixellist
        self.width = len(newpixellist[0])
        self.height = len(newpixellist)
        l = []
        s = ""
        referencepixellist = reference
        row = 0
        for rowlist in newpixellist:
            col = 0
            for pixel in rowlist:
                if newpixellist[row][col] != referencepixellist[row][col]:
                    l.append(newpixellist[row][col][2])
                col += 1
            row += 1
        for i in l:
            s += self.bin_to_letter(i)
        print("The encoded message was as follows: " + s)


# End of PPM Class
