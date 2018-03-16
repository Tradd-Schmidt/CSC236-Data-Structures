'''
Python allows various ways to create and manipulate arrays.
If you use an array of a predetermined size you may encounter a buffer overflow.

From: http://cis1.towson.edu/~cssecinj/modules/cs0/buffer-overflow-cs0-python/
'''

importantData = 1
buffer=[1]*10 #allocates a fixed size space in memory
for i in range(0, 14):
    buffer[i]=7
    print(i)
print("after buffer overflow")
print(importantData)