#include <iostream>
#include "Student.h"
#include "BubbleSort.h"

int main()
{
	Student s[100];
	s[0].InitValue(2003200111, "std1", 3.0);
	s[1].InitValue(2003200101, "std2", 3.2);
	s[2].InitValue(2003200181, "std3", 2.7);

	BubbleSort(s, 3);
	Print(std::cout, s, 3);
}
