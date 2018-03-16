#include <iostream> //needed for cout
using namespace std;

int main()
{
  int chocscale = 7;
  double amount = 10;

  cout << "How much do you like chocolate on a 0-10 scale?" << endl;
  cin >> chocscale;

  cout << "Eating 1.5-3.0 ounces chocolate has health benefits." << endl;
  cout << "How many ounces would you like? " << endl;
  cin >> amount;

  if (chocscale >= 5 && amount >= 3.0)
    {
        cout << "Are you SURE you want that much???" << endl;
    }
  else
    {
        cout << "Are you SURE you do not want even more???" << endl;
    }

  return 0;
}
