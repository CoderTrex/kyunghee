#include "QueType.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

void ReplaceItem(QueType<int> &queue, int oldItem, int newItem){
    QueType<int> tmp;
    int item;
    while (!queue.IsEmpty()){
        queue.Dequeue(item);
        if (item == oldItem){
            tmp.Enqueue(newItem);
        }
        else
            tmp.Enqueue(item);
    }
    while (!tmp.IsEmpty()){
        tmp.Dequeue(item);
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
    original.ReplaceItem(oldone, newone);
    // ReplaceItem(original, oldone, newone);

    for (int i = 0; i < 5; i++){
        original.Dequeue(show);
        cout << show << " ";
    }
}
