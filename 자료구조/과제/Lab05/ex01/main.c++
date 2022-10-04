#include "QueType.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;


int main(){
    int arr[10];
    srand(time(NULL));
    QueType one;
    cout << "random : ";
    for (int i = 0; i < 10; i++){
        int number = rand() % 100;
        arr[i] = number;
        cout << number << " ";
        one.Enqueue(number);
    }
    cout << "\n";
    cout << "Dequeue : ";
    for (int i = 0; i < 10; i++){
        int find_num;
        one.Dequeue(find_num);
        cout << find_num << " ";
    }
}