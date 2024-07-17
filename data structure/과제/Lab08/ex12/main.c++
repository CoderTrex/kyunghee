#include "UnsortedType.h"

int main(){
    UnsortedType<int> list;
    list.InsertItem(2);
    list.InsertItem(4);
    list.InsertItem(9);
    list.InsertItem(6);
    list.PrintSumSquares();
}