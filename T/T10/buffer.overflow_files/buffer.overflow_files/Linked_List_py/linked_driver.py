'''simple driver for LList'''

from LList import LList

print( "Creating linked-list of characters starting with ->h->e->l->l->0->NULL")
testingList = LList("hello")
print("Finding the 4th item in the list: ")
print( testingList.__getitem__(4))
print("alternative coding for finding the 4th item in the list: ")
print(testingList[4])
print("Inserting '!' in the fifth position: ")
testingList.insert(5, '!')
print(testingList[5])

