/******************************************************
    File: printDigit.cpp
    Purpose: This program asks the user for a number
        that is in base 10 and the new number base.
        This program uses recursion to convert the
        number, in which it keeps dividing the number
        by the base until it reaches a number between
        zero and the base, at which point it stops. It
        outputs the digits during that process.
******************************************************/

#include <iostream> // needed for cout and cin
#include <assert.h> // needed for assert() function

using namespace std;

/*----------------------------------------------------
    Recursive function:
    precondition: num and base are both greater than 0.
            Function will check for base > 1.
    postcondition: the digits of num will be output to
            the screen, stopping when most significant
            digit is output.
  ----------------------------------------------------*/
void
printDigits( int num, int base ) {

    assert( base > 1 );     // if base equals zero or one, a seg-fault or FPE will occur.
    if( num < base ) cout << num << " ";
    else {
        printDigits( num / base, base);
        cout << num % base << " ";
    }
}

/*----------------------------------------------------
    driver function:
  ----------------------------------------------------*/
int
main() {
    int num=0;  // the number to convert
    int base=0; // the base to convert the number.
    cout << "What is the number to convert: ";
    cin >> num;
    cout << "What is the new number base for that number: ";
    cin >> base;
    printDigits(num, base);
}
