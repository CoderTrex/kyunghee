#include "sorted.h"
#include <iostream>
using namespace std;


void mergeList(SortedType list1, SortedType list2, SortedType &result){
    ItemType item1, item2;

    list1.ResetList();
    list2.ResetList();
    for (int i = 0; i < list1.LengthIs(); i++){
        list1.GetNextItem(item1);
        result.InsertItem(item1);
    }
    for (int i = 0; i < list2.LengthIs(); i++){
        list1.GetNextItem(item2);
        result.InsertItem(item2);
    }
}