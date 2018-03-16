//Grades computations separated into driver, implementation, and header files
//Reads quiz scores for each student into the two-dimensional array grade (but the input
//code is not shown in this display). Computes the average score for each student and
//the average score for each quiz. Displays the quiz scores and the averages.
#include <iostream>
#include <iomanip>
const int NUMBER_STUDENTS = 4, NUMBER_QUIZZES = 3;

class Grades{

public:

Grades();//Default constructor
//Post-condition: Creates all of the the private member variables, but does not set any values


void setgrades();
//Precondition: Global constant NUMBER_STUDENTS and NUMBER_QUIZZES
//are the dimensions of the array grade.
//Postcondition: Each of the indexed variables grade[st_num-1, quiz_num-1] is et to
//the score for student st_num on quiz quiz_num.


void compute_st_ave();
//Precondition: Global constant NUMBER_STUDENTS and NUMBER_QUIZZES
//are the dimensions of the array grade. Each of the indexed variables
//grade[st_num-1, quiz_num-1] contains the score for student st_num on quiz quiz_num.
//Postcondition: Each st_ave[st_num-1] contains the average for student number stu_num.


void compute_quiz_ave();
//Precondition: Global constant NUMBER_STUDENTS and NUMBER_QUIZZES
//are the dimensions of the array grade. Each of the indexed variables
//grade[st_num-1, quiz_num-1] contains the score for student st_num on quiz quiz_num.
//Postcondition: Each quiz_ave[quiz_num-1] contains the average for quiz numbered
//quiz_num.


void display() const;
//Precondition: Global constant NUMBER_STUDENTS and NUMBER_QUIZZES are the
//dimensions of the array grade. Each of the indexed variables grade[st_num-1,
//quiz_num-1] contains the score for student st_num on quiz quiz_num. Each
//st_ave[st_num-1] contains the average for student stu_num. Each quiz_ave[quiz_num-1]
//contains the average for quiz numbered quiz_num.
//Postcondition: All the data in grade, st_ave, and quiz_ave have been output.


private:
    int grade[NUMBER_STUDENTS][NUMBER_QUIZZES];
    double st_ave[NUMBER_STUDENTS];
    double quiz_ave[NUMBER_QUIZZES];

};
