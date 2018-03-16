/* diceroll.cpp created for CSC 236 Data Structures at Berea College */

#include <iostream>
#include <ctime>
#include <cmath>
#include <cstdlib>
using namespace std;

//---------------------------------------------------------------------
// Program illustrating use of C++ classes called Dice and RandGen
//---------------------------------------------------------------------
class RandGen
{
  public:
    RandGen();                          // set seed for all instances
    int RandInt(int max = RAND_MAX);     // returns int in [0..max)
    int RandInt(int low, int max);      // returns int in [low..max]
    double RandReal();                  // returns double in [0..1)
    double RandReal(double low, double max); // range [low..max]

    static void SetSeed(int seed);      // static (per class) seed set
private:
    static int ourInitialized_;          // for 'per-class' initialization
}; //a semi-colon must end every class declaration.


class Dice
{
  public:
  	Dice(); 				// default constructor assumes a 6-sided die.
    Dice(int sides);        // constructor for any size dice
    int Roll();             // return the random roll of the die
    int NumSides() const;   // how many sides this die has
    int NumRolls() const;   // # times this die rolled

  private:
    int myRollCount_;        // # times die rolled
    int mySides_;            // # sides on die
}; //a semi colon must end every class declaration.

//---------------------------------------------------------------------
// main begins here
//---------------------------------------------------------------------


//---------------------------------------------------------------------
// RandGen class functions begin here
//---------------------------------------------------------------------

int RandGen::ourInitialized_ = 0;

void RandGen::SetSeed(int seed)
// postcondition: system srand() used to initialize seed
//                once per program (This is a static function)
{
    if (0 == ourInitialized_)
    {
    ourInitialized_ = 1;   // only call srand once
	srand(seed);          // randomize
    }
}


RandGen::RandGen()
// postcondition: system srand() used to initialize seed
//                once per program
{
    if (0 == ourInitialized_)
    {
    	ourInitialized_ = 1;          // only call srand once
        srand(unsigned(time(0)));    // randomize
    }
}

int RandGen::RandInt(int max)
// precondition: max > 0
// postcondition: returns int in [0..max)
{
    return int(RandReal() * max);
}

int RandGen::RandInt(int low, int max)
// precondition: low <= max
// postcondition: returns int in [low..max]
{
    return low + RandInt(max-low+1);
}

double RandGen::RandReal()
// postcondition: returns double in [0..1)
{
    return rand() / (double(RAND_MAX) + 1);
}

double RandGen::RandReal(double low, double high)
{
    double width = fabs(high-low);
    double thelow = low < high ? low : high;
    return RandReal()*width + thelow;
}

//---------------------------------------------------------------------
// Dice class functions begin here
//---------------------------------------------------------------------

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


