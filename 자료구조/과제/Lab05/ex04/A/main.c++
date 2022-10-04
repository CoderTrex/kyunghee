#include "QueType.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

int Length(QueType queue){
    int i = 0, num;
    while (!queue.IsEmpty()){
        queue.Dequeue(num);
        i++;
    }
    return i;
}

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

    int one_len = Length(one);
    int two_len = Length(two);
    cout << "one len : " << one_len << "\n" << "two len : " << two_len << "\n";
}