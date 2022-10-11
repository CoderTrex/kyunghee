#include "SortedType.h"

void MergeLists(SortedType<int> &l_a, SortedType<int> &l_b, SortedType<int> &result) {
	int item;

	l_a.ResetList();
	l_b.ResetList();
	for (int i = 0; i < l_a.LengthIs(); i++) {
		l_a.GetNextItem(item);
		result.InsertItem(item);
	}
	for (int i = 0; i < l_b.LengthIs(); i++) {
		l_b.GetNextItem(item);
		result.InsertItem(item);
	}
	l_a.ResetList();
	l_b.ResetList();
}

int main() {
	SortedType<int> s1, s2, s3, s4;

	for (int i = 0; i < 20; i++) {
		if (i % 2 == 0) {
			s1.InsertItem(i);
		} else {
			s2.InsertItem(i);
		}
	}

	std::cout << "========= Sorted List =========\n";
	std::cout << "s1: ";
	s1.Print();
	std::cout << "s2: ";
	s2.Print();
	std::cout << "merged by member function\n";
	s1.MergeLists(s2, s3);
	s3.Print();

	std::cout << "merged by client function\n";
	MergeLists(s1, s2, s4);
	s4.Print();
}
