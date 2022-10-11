#include "UnsortedType.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

template<class ItemType>
void MergeLists(SortedType<ItemType> &l_a,SortedType<ItemType> &l_b, SortedType<ItemType> &result);

template<class ItemType>
int main(){
    srand(time(NULL));
    UnsortedType<ItemType> original_a, original_b, result;
    cout << "pushed num : ";
    for (int i=0; i < 10; i+=2){
        original_a.InsertItem(i);
    }
    for (int i=9; i > 0; i-=2){
        original_b.InsertItem(i);
    }
    cout << "\nOldItem and NewITem" << "\n";
    int oldone, newone;
    cin >>oldone >> newone;
    MergeLists(original_a, original_b, result);
    for (int i = 0; i < 5; i++){
        cout << original.Top() << " ";
        original.Pop();
    }
}

template<class ItemType>
void MergeLists(SortedType<ItemType> &l_a,SortedType<ItemType> &l_b, SortedType<ItemType> &result){
};