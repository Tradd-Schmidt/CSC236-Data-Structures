# ListNode.py
#
# by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014

class ListNode(object):
    
    def __init__(self, item = None, link = None):

        '''creates a ListNode with the specified data value and link
        post: creates a ListNode with the specified data value and link'''
        
        self.item = item
        self.link = link

