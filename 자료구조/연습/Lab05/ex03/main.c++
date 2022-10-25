#include "QueType.h"
#include <iostream>
using namespace std;

void ReplaceItem(QueType &queue, int oldItem, int newItem){
    QueType temp;
    int item;
    while (!queue.IsEmpty()){
        queue.Dequeue(item);
        if (oldItem == item){
            temp.Enqueue(newItem);
        }else{
            temp.Enqueue(item);
        }
    }
    while (!temp.IsEmpty()){
        temp.Dequeue(item);
        queue.Enqueue(item);
    }
}

bool Identical(QueType que1, QueType que2){
    int item1, item2;
    while (!que1.IsEmpty() && !que2.IsEmpty()){
        que1.Dequeue(item1);
        que2.Dequeue(item2);
        if (item1 != item2)
            return false;
    }
    if (que1.IsEmpty() && que2.IsEmpty())
        return true;
    else
        return false;
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
    queue2.Enqueue(10);
    queue2.Enqueue(1);
    queue2.Enqueue(3);
    queue2.Enqueue(35);
    queue2.Enqueue(18);
    queue2.Enqueue(19);
    if (Identical(queue1, queue2))
        cout << "same" << endl;
    else
        cout << "not same" << endl;
    ReplaceItem(queue1, 10, 29);
    if (Identical(queue1, queue2))
        cout << "same" << endl;
    else
        cout << "not same" << endl;
}