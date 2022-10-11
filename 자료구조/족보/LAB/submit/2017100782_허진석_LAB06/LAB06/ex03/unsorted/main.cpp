#include "UnsortedType.h"


void MergeLists(UnsortedType<int> &ul_a, UnsortedType<int> &ul_b, UnsortedType<int> &result)
{
	int item;

	ul_a.ResetList();
	ul_b.ResetList();
	for (int i = 0; i < ul_a.LengthIs(); i++) {
		ul_a.GetNextItem(item);
		result.InsertItem(item);
	}
	for (int i = 0; i < ul_b.LengthIs(); i++) {
		ul_b.GetNextItem(item);
		result.InsertItem(item);
	}
	ul_a.ResetList();
	ul_b.ResetList();
}

int main() {
	UnsortedType<int> u1, u2, u3, u4;

	for (int i = 0; i < 20; i++) {
		if (i % 2 == 0) {
			u1.InsertItem(i);
		} else {
			u2.InsertItem(i);
		}
	}
	std::cout << "========= Unsorted List =========\n";
	std::cout << "u1: ";
	u1.Print();
	std::cout << "u2: ";
	u2.Print();
	std::cout << "merged by member function\n";
	u1.MergeLists(u2, u3);
	u3.Print();

	std::cout << "merged by client function\n";
	MergeLists(u1, u2, u4);
	u4.Print();
}
