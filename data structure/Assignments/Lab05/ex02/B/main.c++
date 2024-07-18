#include "QueType.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

int main(){
    int arr[10];
    srand(time(NULL));
    QueType one;
    cout << "Random : ";
    for (int i = 0; i < 10; i++){
        int number = rand() % 100;
        arr[i] = number;
        cout << number << " ";
        one.Enqueue(number);
    }
    int oldItem, newItem;
    cout << "\n" << "input oldItme and newItem" << "\n";
    cin >> oldItem >> newItem;

    one.ReplaceItem(oldItem, newItem);

    cout << "Replace : ";
    for (int i = 0; i < 10; i++){
        int find_num;
        one.Dequeue(find_num);
        cout << find_num << " ";
    }
}