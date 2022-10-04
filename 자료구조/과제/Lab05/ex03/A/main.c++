#include "QueType.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

bool Identical(QueType queue1, QueType queue2){
    for (int i = 0; i < 10; i++){
        int check_1, check_2;
        queue1.Dequeue(check_1);
        queue2.Dequeue(check_2);
        if (check_1 != check_2)
            return false;
    }
    return true;
}


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

    if (Identical(one, same))
        cout << "same!" << endl;
    else
        cout << "different!" << endl;

    if (Identical(one, different))
        cout << "same!" << endl;
    else
        cout << "different!" << endl;

}