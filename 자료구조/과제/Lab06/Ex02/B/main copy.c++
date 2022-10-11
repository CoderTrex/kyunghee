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
    original.ReplaceItem(oldone, newone);
    
    for (int i = 0; i < 5; i++){
        original.Dequeue(show);
        cout << show << " ";
    }
}