#-------------------------------------------------------------------------------
# Name:        Compressor
# Purpose:  It defines a class called Compressor that interacts with a Hopper
#           to compress coal and make diamonds.
#
# Created:     31/08/2014
#-------------------------------------------------------------------------------

import random
class Compresser(object):
    ''' This class defines a crusher object that will take coal from a hopper object and
    compresses it to make diamonds'''

    DIAMOND_CHANCES = 5     # the chance that a diamond will form is CONSTANT to ALL compressors
    CAPACITY = 10           # ALL compressors have the same capacity

    def __init__(self):
        self.number_diamonds = 0
        self.number_compressed = 0

    def get_coal( self, in_hopper ):
        '''pre: in_hopper is an object of type of Hopper
           post: the amount of coal in in_hopper is decreased and this object is
                set to be full so that it will compress. '''
        if(in_hopper.amount_coal() > self.CAPACITY):
            in_hopper.drain_coal(self.CAPACITY)    # call the method to subtract coal
            self.full = True

    def compress(self):
        '''post: if the compressor is full, it compresses it and possibly creates a diamond.
            number_compressed is incremented, and the compressor is set to no longer be full.'''
        if( self.full ):
            self.number_compressed = self.number_compressed + 1
            # now check to see if we can make a diamond
            if( random.randrange(0,100) < self.DIAMOND_CHANCES ):
                self.number_diamonds = self.number_diamonds + 1
        self.full = False   # Now that we compressed, we are empty


    def __str__(self):
        ''' String representation
        post: returns the string with the amout of diamonds'''
        return "The compressor has made "+str(self.number_diamonds)+" diamonds compressing "+str(self.number_compressed)+" loads of coal."

