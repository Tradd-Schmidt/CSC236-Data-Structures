#include <stdlib.h>	// library with NULL defined
// ListNode.cpp
class ListNode {
    public:		// True object oriented programming would "hide" these instance variables
    char item;		// C++ requires these to be declared at the top
	ListNode* link; 	// These are references, also called pointers

    ListNode( char in_item = '\0', ListNode* in_link = NULL) {

        /*creates a ListNode with the specified data value and link
        post: creates a ListNode with the specified data value and link
		Note that the default value for item is zero and link is
		a special C++ keyword NULL */

        item = in_item;
        link = in_link;
	}
};
