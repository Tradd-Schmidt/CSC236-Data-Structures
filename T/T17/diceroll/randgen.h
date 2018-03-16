#ifndef RANDGEN_H_INCLUDED
#define RANDGEN_H_INCLUDED
#include <cstdlib>

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


#endif // RANDGEN_H_INCLUDED
