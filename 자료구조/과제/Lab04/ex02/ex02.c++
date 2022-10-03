#include <iostream>
#include "StackTType.h"
using namespace std;


void Stack_cp(StackType<int> original, StackType<int> &copy){
    StackType<int> Stack_tmp;
    int check = 0;
    for (int i = 0; i < 5; i++){
        int value =  original.Top();
        original.Pop();
        Stack_tmp.Push(value);
    }
    for (int i = 0; i < 5; i++){
        int value =  Stack_tmp.Top();
        Stack_tmp.Pop();
        copy.Push(value);
    }
}

int main(){
    StackType<int> stack_original, Stack_copy;
    
    for (int i = 0; i < 5; i++){
        stack_original.Push(i);
    }
    Stack_cp(stack_original, Stack_copy);

    cout << "this is original stack : ";    
    for (int i = 0; i < 5; i++){
        int show =  stack_original.Top();
        stack_original.Pop();
        cout << show << " ";
    }
    
    cout << "\n";

    cout << "this is copy stack : ";    
    for (int i = 0; i < 5; i++){
        int show =  Stack_copy.Top();
        Stack_copy.Pop();
        cout << show << " ";
    }
}