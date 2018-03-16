#test_hand.py
#
# by David M. Reed and John Zelle
# from Data Structures and Algorithms Using Python and C++
# downloaded from publisher's website:
# https://www.fbeedle.com/content/data-structures-and-algorithms-using-python-and-c
# on July 23, 2014

from Hand import Hand
from Card import Card
h = Hand("North")
h.add(Card(5,"c"))
h.add(Card(10,"d"))
h.add(Card(13,"s"))
h.dump()
h.sort()
h.dump()
