#include <iostream>

class DayOfYear{
public:

    void input();

    void output();

    void set(int new_month, int new_day);

    int get_month();

    int get_day();

private:
    void check_date();
    int month;
    int day;

};
