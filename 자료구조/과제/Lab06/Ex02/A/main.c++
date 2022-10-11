#include "QueType.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

void ReplaceItem(QueType<int> &queue, int oldItem, int newItem){
    QueType<int> temp_Queue; // 백업용 스텍
    int temp_Item; // top을 받는 아이템

    while (!queue.IsEmpty()){
        queue.Dequeue(temp_Item);
        if (temp_Item == oldItem){
            temp_Queue.Enqueue(newItem);
        }
        else{
            temp_Queue.Enqueue(temp_Item);
        }
    }
    while (!temp_Queue.IsEmpty()){
        int item;
        temp_Queue.Dequeue(item);
        queue.Enqueue(item);
    }
}

int main(){
    srand(time(NULL));
    QueType<int> original;
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
