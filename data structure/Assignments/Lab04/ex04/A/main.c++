#include "StackType.h"
#include <iostream>
using namespace std;



void ReplaceItem(StackType &st, int oldItem, int newItem);

int main(){
    StackType stack;
    stack.Push(10);
    stack.Push(8);
    stack.Push(7);
    stack.Push(10);
    stack.Push(9);

    int newItem, oldItem, item;

    cout << "바꿀 아이템과 바꾸고 싶은 아이템을 순서대로 입력하세요\n";
    cin >> oldItem >> newItem;

    ReplaceItem(stack, oldItem, newItem);
    while(!stack.IsEmpty()){
        item = stack.Top();
        stack.Pop();
        cout << "Item : "<< item << endl; 
    } 
    return 0;
}

void ReplaceItem(StackType &st, int oldItem, int newItem){
    StackType stack_tmp;
    for (int i = 0; i < 5; i++){
        int value = st.Top();
        if (st.Top() == oldItem){
            stack_tmp.Push(newItem);
        }
        else
            stack_tmp.Push(value);
        st.Pop();
    }
    for (int i = 0; i < 5; i++){
        int value = stack_tmp.Top();
        st.Push(value);
        stack_tmp.Pop();
    }
}