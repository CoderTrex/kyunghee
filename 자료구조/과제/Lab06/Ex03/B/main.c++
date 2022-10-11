#include "sortedType.h"
#include <iostream>
#include <cstddef>
#include <stdlib.h>
#include <time.h>
using namespace std;


int main(){
    SortedType<int> original_a, original_b, result;
    for (int i=0; i < 10; i++){
        if (i % 2 == 0)
            original_a.InsertItem(i);
        else
            original_b.InsertItem(i);
    }
    
    original_a.MergeLists(original_b, result);
    result.ResetList();
    int num;
    for (int i = 0; i < 10; i++){
        result.GetNextItem(num);
        cout << num << " ";
    }
}