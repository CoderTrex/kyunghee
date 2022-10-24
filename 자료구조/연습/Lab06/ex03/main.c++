#include "SortedType.h"
#include <iostream>
#include <stdlib.h>
using namespace std;

void MergeLists(SortedType<int> &l_a, SortedType<int> &l_b, SortedType<int> &result){
    l_a.ResetList();
    l_b.ResetList();
    int a_len = l_a.LengthIs(), b_len = l_b.LengthIs(), item;
    
    while (a_len-- > 0){
        l_a.GetNextItem(item);
        result.InsertItem(item);
    }
    while (b_len-- > 0){
        l_b.GetNextItem(item);
        result.InsertItem(item);
    }
}



int main(){
    SortedType<int> original_a, original_b, result;
    for (int i=0; i < 10; i++){
        if (i % 2 == 0)
            original_a.InsertItem(i);
        else
            original_b.InsertItem(i);
    }
    
    MergeLists(original_a, original_b, result);
    result.ResetList();
    int num;
    for (int i = 0; i < 10; i++){
        result.GetNextItem(num);
        cout << num << " ";
    }
}