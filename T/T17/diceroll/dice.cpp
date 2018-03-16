#include "dice.h"
#include "randgen.h"
using namespace std;

Dice::Dice()//Default is to assume a six sided die.
// postcondition: all private fields initialized
{
    myRollCount_ = 0;
    mySides_ = 6;
}


Dice::Dice(int sides)
// postcondition: all private fields initialized
{
    myRollCount_ = 0;
    mySides_ = sides;
}

int Dice::Roll()
// postcondition: number of rolls updated
//                random 'die' roll returned
{
    RandGen gen;    // random number generator

    myRollCount_= myRollCount_ + 1;         // update # of times die rolled
    return gen.RandInt(1,mySides_);        // in range [1..mySides_]
}

int Dice::NumSides() const
// postcondition: return # of sides of die
{
    return mySides_;
}

int Dice::NumRolls() const
// postcondition: return # of times die has been rolled
{
    return myRollCount_;
}


