# test_Deck.py
#
# by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014

from Deck import Deck

d = Deck() 
print d.deal()
print d.deal()
print d.deal()
d.shuffle()
print d.size()
print d.deal()
print d.deal()
