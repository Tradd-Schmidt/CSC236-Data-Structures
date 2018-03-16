// I added some code to check the user's birthday to Bach's Birthday.
// I then print who would be older if Bach was born the same year that the user was born

#include <iostream>
#include "stdlib.h"
#include "smallclass.h"
using namespace std;

int main( )
{
    DayOfYear today, bach_birthday;
    cout << "Enter today's date:\n";
    today.input( );
    cout << "Today's date is ";
    today.output( );

    bach_birthday.set(3, 21);
    cout << "J. S. Bach's birthday is ";
    bach_birthday.output( );

    if ( today.get_month( ) == bach_birthday.get_month( ) &&
               today.get_day( ) == bach_birthday.get_day( ) )
        cout << "Happy Birthday Johann Sebastian!\n";
    else
        cout << "Happy Unbirthday Johann Sebastian!\n";

    DayOfYear user_birthday;
    cout << "Enter your birthday month and year:\n";
    user_birthday.input();


    if (bach_birthday.get_month() < user_birthday.get_month()){
        cout << "If Bach was born the same year as you, he would be older\n";
    }
    else if (bach_birthday.get_month() > user_birthday.get_month()){
        cout << "If Bach was born the same year as you, you would be older.\n";
    }

    else{
        if (bach_birthday.get_day() < user_birthday.get_day())
            cout << "If Bach was born the same year as you, he would be older\n";
        else if (bach_birthday.get_day() > user_birthday.get_day())
            cout << "If Bach was born the same year as you, you would be older.\n";
        else
            cout << "If Bach was born the same year as you, you would have been born on the same day as him!";
    }
    return 0;
}
