#include "SortedType.h"
using namespace std;

int main(){
    SortedType<int> sort_l;
    for (int i = 0; i < 3; i++){
        sort_l.InsertItem(i);
    }
    sort_l.PrintReverse();
}