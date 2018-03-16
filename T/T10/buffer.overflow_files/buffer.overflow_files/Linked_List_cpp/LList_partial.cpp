// LList_partial.cpp
// This file is almost a direct translation of the same LList object
// in Python. There were a lot of libraries to include, such as assert.h
// in order to enable the assert function for testing.
//
#include "ListNode.cpp"	// This file contains library reference for NULL
#include <string>	// Assume that this linked list inputs a string of numbers
#include <assert.h> // this library is needed for the assert() function.
using namespace std;
class LList {
	ListNode* head;	// Remember, C++ requires us to declare these instance variables
	int size;		//   up front.
    //------------------------------------------------------------
public:
    LList() {
        head = NULL;
        size = 0;
    }

    LList(string seq="") {

        //create an LList
        //post: creates a list containing items in seq
		if( seq.length() == 0 ) {
            // No items to put in, create an empty list
			head = NULL;
		}
        else {
            // Create a node for the first item
            head = new ListNode(seq[0], NULL);

            // Add remaining items keeping track of last node added
            ListNode* last = head;
            for( int i=1; i<seq.length(); i++) {
                last->link = new ListNode(seq[i], NULL);
                last = last->link;
			}
        }
        size = seq.length();
    }
    //------------------------------------------------------------

    ListNode* __getitem__( int position ) {

        /*private method that returns node that is at location position
        in the list (0 is first item, size-1 is last item)
        pre: 0 <= position < self.size
        post: returns the ListNode at the specified position in the
        list'''*/

        assert( (0 <= position) && ( position < size ) );

        ListNode* node = head;
        // move forward until we reach the specified node
        for( int i=0; i<position; i++ ) {
            node = node->link;
		}
        return node;
	}
    //------------------------------------------------------------

    void insert(int i, char x){

        /*inserts x at position i in the list
        pre: 0 <= i <= self.size
        post: x is inserted into the list at position i and
              old elements from position i..oldsize-1 are at positions
              i+1..newsize-1*/

        assert( (0 <= i) && (i<= size) );

        if( i == 0 ) {
            // insert before position 0 requires updating self.head
            head = new ListNode(x, head);
		}
        else {
            // getitem  that node is to be insert after
            ListNode* node = __getitem__(i - 1);
            node->link = new ListNode(x, node->link);
		}
        size += 1;
	}
    //------------------------------------------------------------

};
