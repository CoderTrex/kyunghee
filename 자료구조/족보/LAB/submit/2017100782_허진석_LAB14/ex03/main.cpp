#include "Student.h"

void SelectionSortPointer(Student* values[], int numValues) {
	for (int i = 0; i < numValues; i++) {
		int min_std = i;

		for (int j = i; j < numValues; j++) {
			if (*values[j] < *values[min_std]) {
				min_std = j;
			}
		}
		Swap(values[i], values[min_std]);
	}
}

void PrintByPointer(Student *values[], int numValues) {
	for (int i = 0; i < numValues; i++)
		values[i]->Print(std::cout);
}
 
int main() {
	Student s[10];
	Student *p[10];
	int len = 7;

	s[0].InitValue(9, "inadf", 3.8);
	s[1].InitValue(2, "sa", 3.2);
	s[2].InitValue(1, "naha", 3.4);
	s[3].InitValue(8, "john", 4.1);
	s[4].InitValue(5, "alal", 4.3);
	s[5].InitValue(0, "fifi", 3.5);
	s[6].InitValue(7, "phia", 3.1);

	for (int i = 0; i < len; i++) {
		p[i] = &s[i];
	}

	SelectionSortPointer(p, len);
	PrintByPointer(p, len);
}
