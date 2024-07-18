#include "UnsortedType.h"
#include <iostream>
#include <cstddef>
#include <stdlib.h>
#include <time.h>
using namespace std;


void MergeLists(UnsortedType<int> &unsort_a, UnsortedType<int> &unsort_b, UnsortedType<int> &result) {
	int item;

	unsort_a.ResetList();
	unsort_b.ResetList();
	for (int i = 0; i < unsort_a.LengthIs(); i++) {
		unsort_a.GetNextItem(item);
		result.InsertItem(item);
	}
	for (int i = 0; i < unsort_b.LengthIs(); i++) {
		unsort_b.GetNextItem(item);
		result.InsertItem(item);
	}
	unsort_a.ResetList();
	unsort_b.ResetList();
}

int main(){
    UnsortedType<int> original_a, original_b, result;
    original_a.InsertItem(10);   
    original_a.InsertItem(3);   
    original_a.InsertItem(7);  
    original_a.InsertItem(6);   
    original_a.InsertItem(20);   
    original_b.InsertItem(3);   
    original_b.InsertItem(1);  
    original_b.InsertItem(40);  
    MergeLists(original_a, original_b, result);
    result.ResetList();
    int num;
    for (int i = 0; i < 10; i++){
        result.GetNextItem(num);
        cout << num << " ";
    }
}