# Stack.py
#
# by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014
import random


class Stack(object):

    # ------------------------------------------------------------

    def __init__(self):

        '''post: creates an empty LIFO stack'''

        self.items = []

    # ------------------------------------------------------------

    def push(self, item):
        
        '''post: places x on top of the stack'''

        self.items.append(item)

    # ------------------------------------------------------------

    def pop(self):

        '''post: removes and returns the top element of 
        the stack'''

        return self.items.pop()

    # ------------------------------------------------------------

    def top(self):

        '''post: returns the top element of the stack without 
        removing it'''

        try:
            return self.items[-1]
        except:
            return self.items[0]

    # ------------------------------------------------------------

    def size(self):

        '''post: returns the number of elements in the stack'''

        return len(self.items)

    def shuffle(self):
        """
        Randomizes the order of all items in the stack
        :return: None
        """
        random.shuffle(self.items)

    def clear(self):    # This was the function I added
        """
        Completely empties the items
        :return: None
        """
        del self.items[:]
