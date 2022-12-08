#include "MergeSort.h"
#include <iostream>

int main() {
	Student s[50];

	s[0].InitValue(9, "inadf", 3.8);
	s[1].InitValue(2, "sa", 3.2);
	s[2].InitValue(1, "naha", 3.4);
	s[3].InitValue(8, "john", 4.1);
	s[4].InitValue(5, "alal", 4.3);
	s[5].InitValue(0, "fifi", 3.5);
	s[6].InitValue(7, "phia", 3.1);

	MergeSort(s, 0, 6);
	for (int i = 0; i < 6; i++) {
		s[i].Print(std::cout);
	}
}
