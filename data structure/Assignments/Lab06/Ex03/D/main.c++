#include "UnsortedType.h"
#include <iostream>
#include <cstddef>
#include <stdlib.h>
#include <time.h>
using namespace std;


int main(){
    UnsortedType<int> original_a, original_b, result;
    int num;

    original_a.InsertItem(10);   
    original_a.InsertItem(3);   
    original_a.InsertItem(7);  
    original_a.InsertItem(6);   
    original_b.InsertItem(4);  
    original_b.InsertItem(1); 
    original_b.InsertItem(40);  
    original_b.InsertItem(18);   
    original_a.MergeLists(original_b, result);
    result.ResetList();
    for (int i = 0; i < result.LengthIs(); i++){
        result.GetNextItem(num);
        cout << num << " ";
    }
}