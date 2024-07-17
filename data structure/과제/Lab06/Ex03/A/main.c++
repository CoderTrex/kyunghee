#include "sortedType.h"
#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;


void MergeLists(SortedType<int> &sort_a, SortedType<int> &sort_b, SortedType<int> &result){
	int item;

	sort_a.ResetList();
	sort_b.ResetList();
	for (int i = 0; i < sort_a.LengthIs() + sort_b.LengthIs(); i++) {
		if (i % 2 == 0){
            sort_a.GetNextItem(item);
            result.InsertItem(item);
        }
        else{
            sort_b.GetNextItem(item);
            result.InsertItem(item);
        }
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


// 	SortedType<int> s1, s2, s3, s4;

// 	for (int i = 0; i < 20; i++) {
// 		if (i % 2 == 0) {
// 			s1.InsertItem(i);
// 		} else {
// 			s2.InsertItem(i);
// 		}
// 	}

// 	std::cout << "========= Sorted List =========\n";
// 	std::cout << "s1: ";
// 	s1.Print();
// 	std::cout << "s2: ";
// 	s2.Print();
// 	std::cout << "merged by member function\n";
// 	s1.MergeLists(s2, s3);
// 	s3.Print();

// 	std::cout << "merged by client function\n";
// 	MergeLists(s1, s2, s4);
// 	s4.Print();
// }
}