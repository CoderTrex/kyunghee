#include "QueType.h"
#include <iostream>
using namespace std;

int main(){
    QueType queue;
    int item;
    queue.Enqueue(10);
    queue.Enqueue(1);
    queue.Enqueue(3);
    queue.Enqueue(35);
    queue.Enqueue(18);
    queue.Enqueue(19);
    for (int i =0; i < 6; i++){
        queue.Dequeue(item);
        cout << item << " ";
    }
}