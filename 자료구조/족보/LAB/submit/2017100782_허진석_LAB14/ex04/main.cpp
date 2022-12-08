#include "HashTable.h"
#include <iostream>

int main() {
	Student s[50];
	HashTable<Student> ht;

	bool found = false;
	s[0].InitValue(9, "inadf", 3.8);
	s[1].InitValue(2, "sa", 3.2);
	s[2].InitValue(1, "naha", 3.4);
	s[3].InitValue(8, "john", 4.1);
	s[4].InitValue(5, "alal", 4.3);
	s[5].InitValue(0, "fifi", 3.5);
	s[6].InitValue(7, "phia", 3.1);
	s[7].InitValue(11, "inadf", 3.8);
	s[8].InitValue(13, "sa", 3.2);
	s[9].InitValue(24, "naha", 3.4);
	s[10].InitValue(17, "john", 4.1);
	s[11].InitValue(18, "alal", 4.3);
	s[12].InitValue(19, "fifi", 3.5);
	s[13].InitValue(20, "phia", 3.1);
	s[14].InitValue(16, "inadf", 3.8);
	s[15].InitValue(6, "sa", 3.2);
	s[16].InitValue(12, "naha", 3.4);
	s[17].InitValue(15, "john", 4.1);
	s[18].InitValue(14, "alal", 4.3);
	s[19].InitValue(27, "fifi", 3.5);
	s[20].InitValue(4, "phia", 3.1);

	for (int i = 0; i < 21; i++)
		ht.InsertItem(s[i]);

	ht.RetrieveItem(s[5], found);
	if (found)
		s[5].Print(std::cout);
	ht.RetrieveItem(s[7], found);
	if (found)
		s[7].Print(std::cout);
}
