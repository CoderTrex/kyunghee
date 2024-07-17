#include "StackType.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

void ReplaceItem(StackType &stack, ItemType oldItem, ItemType newItem);

int main(){
    srand(time(NULL));
    StackType original;
    cout << "pushed num : ";
    for (int i=0; i < 5; i++){
        int a;
        a = rand() % 10;
        original.Push(a);
        cout << a << " ";
    }

    cout << "\nOldItem and NewITem" << "\n";
    int oldone, newone;
    cin >>oldone >> newone;
    ReplaceItem(original, oldone, newone);

    for (int i = 0; i < 5; i++){
        cout << original.Top() << " ";
        original.Pop();
    }
}

void ReplaceItem(StackType &stack, ItemType oldItem, ItemType newItem){
    StackType temp_stack; // 백업용 스텍
    ItemType temp_Item; // top을 받는 아이템

    while (!stack.IsEmpty()){
        temp_Item = stack.Top();

        if (temp_Item == oldItem){
            temp_stack.Push(newItem);
            stack.Pop();
        }
        else{
            temp_stack.Push(temp_Item);
            stack.Pop();
        }
    }
    while (!temp_stack.IsEmpty()){
        temp_Item = temp_stack.Top();
        stack.Push(temp_Item);
        temp_stack.Pop();
    }
}