#include "StackType.h"
#include <iostream>
using namespace std;




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

    stack.RepalceItem(oldItem, newItem);
    while(!stack.IsEmpty()){
        item = stack.Top();
        stack.Pop();
        cout << "Item : "<< item << endl; 
    } 
    return 0;
}
