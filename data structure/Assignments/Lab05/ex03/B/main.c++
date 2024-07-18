#include "QueType.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

int main(){
    srand(time(NULL));
    QueType one, same, different;
    cout << "one and same value : ";
    for (int i = 0; i < 10; i++){
        int number = rand() % 100;
        cout << number << " ";
        one.Enqueue(number);
        same.Enqueue(number);
    }

    cout << "\n" << "different value : ";
    for (int i = 0; i < 10; i++){
        int number = rand() % 100;
        cout << number << " ";
        different.Enqueue(number);
    }
    cout << "\n";

    if (one.Identical(same))
        cout << "same!" << endl;
    else
        cout << "different!" << endl;

    if (one.Identical(different))
        cout << "same!" << endl;
    else
        cout << "different!" << endl;

}