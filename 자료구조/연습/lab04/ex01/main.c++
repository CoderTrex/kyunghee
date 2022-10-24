#include "StackTType.h"
#include <iostream>
using namespace std;


int main(){
    StackType<int> stack, stack_tmp, stack_copy;
    int num;
    for (int i = 0; i < 5; i++){
        stack.Push(i);
    }
    for (int j = 0; j < 5; j++){
        num = stack.Top();
        stack.Pop();
        stack_tmp.Push(num);
    }
    for (int i = 0; i < 5; i++){
        num = stack_tmp.Top();
        stack_tmp.Pop();
        stack.Push(num);
        stack_copy.Push(num);
    }
    for (int i = 0; i < 5; i++){
        num = stack_copy.Top();
        stack_copy.Pop();
        cout << num << " ";
    }
}