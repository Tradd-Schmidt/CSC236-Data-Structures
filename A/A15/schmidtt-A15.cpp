// Binary Search Tree
// Originally created by Dr. Jan Pearce
// Modified by Mario Nakazawa

// Your name: PUT YOUR NAME(S) HERE
// Tradd Schmidt
//    NOTE THAT THIS VERSION NO LONGER COMPLETELY MATCHES THE VERSION
//    IN THE ASSIGNMENT. Namely, duplicates are no longer inserted
//    into the tree, and a lot of comments are included in this code.

// Purpose: to build a binary search tree from a users input and then
// print out the different traversal notations using that search tree

#include<iostream>
using namespace std;

// This class is really just a struct because it is a bag of variable
// and information without any functionality built into it. It
// represented a single node in the binary search tree, holding the
// value of the node, and pointers to the left and right children,
// respectively.
class BstNode
{
public:
  int data;
  BstNode* left;
  BstNode* right;
};

// precondition: none, as any value, positive or negative, will
// work. The value must be an integer though, as specified in the data
// type of the parameter.
// postcondition: a new object of type BstNode will be created with the
// value of data, and it is a leaf (i.e. has NULL values for both left
// and right children).
BstNode*
GetNewNode(int data)
{
	BstNode* newNode = new BstNode();
	newNode->data = data;
	newNode->left = NULL;
	newNode->right = NULL;
	return newNode;
}

// This function seems counterintuitive. Notice that the base case
// would create the node, but then this function returns the reference
// to that node, which is assigned to the left or right child of the
// node that called this function. This relationship ripples back to
// the original called function, which would return the root of the tree.
// precondition: none
// postcondition: If the values does not exist in the tree, it is
// inserted and the pointer to the root of the tree is eventually
// returned.
BstNode*
insert(BstNode* thisNode, int data)
{
  // BASE CASE: If the current location is empty, then create a new
  // node with that value.
  if( thisNode == NULL) {
    thisNode = GetNewNode(data);
  }

  // RECURSIVE CALL 1: If the value we want to insert is less than
  // where we are, then go down the left child recursively.
  else if(data < thisNode->data) {
    thisNode->left = insert( thisNode->left, data );    // Recursive expression
  }

  // RECURSIVE CALL 2: If the value is greater than where we are now,
  // go down the right child and make sure that the
  else if( data > thisNode->data) {
    thisNode->right = insert( thisNode->right, data );    // Recursive expression
  }

  // Note that if the value already exists in the tree, we ignore it.

  // this function ends by returning the current node
  return thisNode;
}

// PUT YOUR rawinput() FUNCTION BELOW
BstNode*
rawinput()
/** \brief Takes 10 different integer inputs from the user to be inserted into a binary search tree
 *
 * \return a pointer to the root of the binary search tree
 *
 */

{
    BstNode* head = NULL;
    int num;
    for (int i = 10; i > 0; i--)
    {
        cout << "Please provide an integer to input into the binary search tree." << endl;
        cin >> num;
        head = insert(head, num);
    }
    return head;
}

// PUT YOUR inorder() FUNCTION BELOW
void
inorder(BstNode* head)
/** \brief Traverses a Binary Search Tree in in-order notation given a node that is the root of a tree
 *
 * \param head is the root of a tree
 * \return void
 *
 */
{
    // Base case is if both left and right node == NULL
    if (head->left != NULL)    // If the left node is not NULL the head becomes the left node
        inorder(head->left);    // Recursive expression

    cout << head->data << " ";

    if (head->right != NULL)    // If the right node is not NULL the head becomes the right node
        inorder(head->right);    // Recursive expression

}

// PUT YOUR preorder() FUNCTION BELOW
void
preorder(BstNode* head)
/** \brief Traverses a Binary Search Tree in pre-order notation given a node that is the root of a tree
 *
 * \param head is the root of a tree
 * \return void
 *
 */

{
    // Base case is if both left and right node == NULL
    cout << head->data << " ";

    if (head->left != NULL)    // If the left node is not NULL the head becomes the left node
        preorder(head->left);    // Recursive expression

    if (head->right != NULL)    // If the right node is not NULL the head becomes the right node
        preorder(head->right);    // Recursive expression

}

// PUT YOUR postorder() FUNCTION BELOW
void
postorder(BstNode* head)
/** \brief Traverses a Binary Search Tree in post-order notation given a node that is the root of a tree
 *
 * \param head is the root of a tree
 * \return void
 *
 */
{
    // Base case is if both left and right node == NULL
    if (head->left != NULL)    // If the left node is not NULL the head becomes the left node
        postorder(head->left);    // Recursive expression

    if (head->right != NULL)    // If the right node is not NULL the head becomes the right node
        postorder(head->right);    // Recursive expression

    cout << head->data << " ";
}

// The main function, which returns a zero if the program runs
// s NewNodeuccessfully to completion.
int main()
{
    BstNode* root = rawinput();

    cout << "Postorder notation: ";
    postorder(root);
    cout << endl;
    cout << "Pre-order notation: ";
    preorder(root);
    cout << endl;
    cout<< "In-order notation: ";
    inorder(root);
    cout << endl;
    return 0;
}
