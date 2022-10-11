#include "StackType.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

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
    cin >> oldone >> newone;
    original.ReplaceItem(oldone, newone);

    for (int i = 0; i < 5; i++){
        cout << original.Top() << " ";
        original.Pop();
    }
}
