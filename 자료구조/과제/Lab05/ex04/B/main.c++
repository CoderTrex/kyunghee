#include "QueType.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

int main(){
    srand(time(NULL));
    QueType one, two;
    int range_one = rand() % 10;
    int range_two = rand() % 10 + 3;

    cout << "one: " << range_one << "\n";
    for (int i=0; i<range_one; i++){
        int number = rand() % 100;
        one.Enqueue(number);
    }
    cout << "two: " << range_two << "\n";
    for (int i=0; i<range_two; i++){
        int number = rand() % 100;
        two.Enqueue(number);
    }
    cout << "\n";

    int one_len = one.Length();
    int two_len = two.Length();
    cout << "one len : " << one_len << "\n" << "two len : " << two_len << "\n";
}