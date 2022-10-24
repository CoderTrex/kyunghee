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
    }
}


int main(){
    QueType queue;
    int item;
    queue.Enqueue(10);
    queue.Enqueue(1);
    queue.Enqueue(3);
    queue.Enqueue(35);
    queue.Enqueue(18);
    queue.Enqueue(19);
    ReplaceItem(queue, 10, 83);
}