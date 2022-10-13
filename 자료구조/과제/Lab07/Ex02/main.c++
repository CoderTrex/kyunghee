#include <iostream>
#include "StackType.h"
using namespace std;

int main(){
    StackType Stack_O, Stack_C;

    for (int i=0; i < 10; i++){
        Stack_O.Push(i);
    }
    Stack_O.Copy(Stack_C);
    for (int i = 0; i < 10; i++){
        cout << Stack_C.Top() << " ";
        Stack_C.Pop(); 
    }
}