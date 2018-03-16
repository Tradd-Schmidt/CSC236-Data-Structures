//Computation of grades a class and separated into driver, implementation, and header files
//Reads quiz scores for each student into the two-dimensional array grade (but the input
//code is not shown in this display). Computes the average score for each student and
//the average score for each quiz. Displays the quiz scores and the averages.
// Conceptually, each row represents the student number less 1
// Conceptually, each columnn represents the quiz number

#include <iostream>
#include <iomanip>
#include "grades.h"

int main( )
{
    using namespace std;

    Grades coursegrades;

    coursegrades.setgrades();
    coursegrades.compute_st_ave();
    coursegrades.compute_quiz_ave();
    coursegrades.display();

    return 0;
}
