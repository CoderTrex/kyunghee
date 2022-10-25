#include "QueType.h"
#include <iostream>
using namespace std;

int Length(QueType queue){
    QueType temp;
    int len = 0, item;
    while (!queue.IsEmpty()){
        queue.Dequeue(item);
        temp.Enqueue(item);
        len++;
    }
    while (!temp.IsEmpty()){
        temp.Dequeue(item);
        queue.Enqueue(item);
    }
    return len;
}

int main(){
    QueType queue1, queue2;
    int item;
    queue1.Enqueue(10);
    queue1.Enqueue(1);
    queue1.Enqueue(3);
    queue1.Enqueue(35);
    queue1.Enqueue(18);
    queue1.Enqueue(19);
    queue1.Enqueue(19);
    cout << queue1.Length() << " ";
    cout << Length(queue1);
}