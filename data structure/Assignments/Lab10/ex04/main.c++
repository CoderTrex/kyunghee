#include "StackTType.h"
#include <iostream>
#include <cstdlib>
#include <time.h>
using namespace std;


int main()
{
    StackType<int> test;
    srand((unsigned int)(time(NULL)));
    test.Push(1, 3);
    test.Push(2, 22);
    test.Push(3, 21);
    test.Push(4, 8);
    test.Push(5, 10);
    test.Push(6, 3);

    test.print();
    test.Pop();
    cout << "------------" << "\n";
    test.print();
    test.Pop();
    cout << "------------" << "\n";
    test.print();
}
