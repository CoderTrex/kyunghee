#include "QueType.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;


void ReplaceItem(QueType &queue, int oldItem, int newItem){
    int arr[10];
    int tmp;
    for (int i = 0; i < 10; i++){
        queue.Dequeue(tmp);
        arr[i] = tmp;
    }
    for (int i = 0; i < 10; i++){
        if (arr[i] == oldItem)
            queue.Enqueue(newItem);
        else
            queue.Enqueue(arr[i]);
    }
}

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
    ReplaceItem(one, oldItem, newItem);

    cout << "Replace : ";
    for (int i = 0; i < 10; i++){
        int find_num;
        one.Dequeue(find_num);
        cout << find_num << " ";
    }
}