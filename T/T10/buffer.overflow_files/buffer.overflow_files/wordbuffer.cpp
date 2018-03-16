/*
Writing outside the bounds of a block of allocated memory can corrupt data, crash the program,
or cause the execution of malicious code. C++ is particularly vulnerable to buffer overflows.

from http://cis1.towson.edu/~cssecinj/modules/cs0/buffer-overflow-cs0-c/
*/
#include <iostream> //for keyboard input and screen output
using namespace std; // needed to simplify standard libraries

int main ()
{
    int buffer=10;
    cout<< "buffer: "<<buffer<<endl;
    for (int i=0; i<=30; i++){
        buffer=buffer*10;
        cout<< "buffer: "<<buffer<<endl;
    }
    cout << "after buffer overflow" << endl;
    cout<< "buffer: "<<buffer<<endl;

    return 0; //this is typical of the last line of a C++ program
}
