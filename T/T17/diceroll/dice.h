#ifndef DICE_H_INCLUDED
#define DICE_H_INCLUDED
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


#endif // DICE_H_INCLUDED
