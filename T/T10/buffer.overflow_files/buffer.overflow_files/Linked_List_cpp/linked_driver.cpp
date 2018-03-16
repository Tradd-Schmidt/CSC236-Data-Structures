#include <iostream>
#include "LList_partial.cpp"
using namespace std;

int main()
{
    cout << "Creating linked-list of characters starting with ->h->e->l->l->0->NULL"<<endl;
    LList testingList = LList("hello");
    cout << "Finding the 4th item in the list: "<<endl;
    cout << testingList.__getitem__(4)->item << endl;
    cout << "Inserting '!' in the fifth position: "<<endl;
    testingList.insert(5, '!');
    cout << testingList.__getitem__(5)->item << endl;
    return 0;
}
