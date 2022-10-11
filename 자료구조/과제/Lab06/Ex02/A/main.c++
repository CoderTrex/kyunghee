#include "QueType.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

template <class ItemType>
void ReplaceItem(QueType<ItemType> &queue, ItemType oldItem, ItemType newItem);

template <class ItemType>
int main(){
    srand(time(NULL));
    QueType<ItemType> original;
    cout << "pushed num : ";
    for (int i=0; i < 5; i++){
        int a;
        a = rand() % 10;
        original.Enqueue(a);
        cout << a << " ";
    }

    cout << "\nOldItem and NewITem" << "\n";
    int oldone, newone;
    int show;
    cin >>oldone >> newone;
    ReplaceItem(original, oldone, newone);

    for (int i = 0; i < 5; i++){
        original.Dequeue(show);
        cout << show << " ";
    }
}

template <class ItemType>
void ReplaceItem(QueType<ItemType> &queue, ItemType oldItem, ItemType newItem){
    QueType<ItemType> temp_Queue; // 백업용 스텍
    ItemType temp_Item; // top을 받는 아이템

    while (!queue.IsEmpty()){
        int item;
        queue.Dequeue(item);

        if (item == oldItem){
            temp_Queue.Enqueue(newItem);
        }
        else{
            temp_Queue.Enqueue(item);
        }
    }
    while (!queue.IsEmpty()){
        int item;
        temp_Queue.Dequeue(item);
        queue.Enqueue(item);
    }
}