#include "StackTType.h"
#include <iostream>
using namespace std;


int main()
{
    StackType<int> test;
    test.Push(10);
    test.Push(9);
    test.Push(8);
    test.Push(7);
    test.Push(6);

    test.print();
    test.Pop();
    test.print();
    test.Pop();
}
