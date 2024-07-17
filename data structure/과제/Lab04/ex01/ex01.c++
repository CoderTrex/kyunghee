#include "StackTType.h"
#include <iostream>
using namespace std;

int main(){
    StackType<int> stack;
    for(int i = 1; i <= 6; i++){
        stack.Push(i);
    }
    for (int i = 0; i < 6; i++){
        int show =  stack.Top();
        stack.Pop();
        cout << show << endl;
    }
}