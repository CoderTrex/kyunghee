#include <iostream>
#include "Student.h"
#include "SelectionSort.h"

int main()
{
	Student s[100];
	s[0].InitValue(2003200111, "std1", 3.0);
	s[1].InitValue(2003200101, "std2", 3.2);
	s[2].InitValue(2003200181, "std3", 2.7);
	s[3].InitValue(2003200181, "std4", 2.7);
	s[4].InitValue(2003200181, "std2", 2.7);

	SelectionSort(s, 5);
	Print(std::cout, s, 5);
}
