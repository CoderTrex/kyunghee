#include "HashTable.h"
#include <iostream>
using namespace std;

int main()
{
    Student stu[10];
    HashTable<Student> stu_table;
	bool find = false;
    stu[1].InitValue(2003200100, (char*)"Ford", 3.3);
    stu[0].InitValue(2004200121, (char*)"smith", 3.0);
    stu[2].InitValue(2005200132, (char*)"donald", 2.7);
    
	for (int i = 0; i < 3; i++)
	{
		stu_table.InsertItem(stu[i]);
	}
	stu_table.RetrieveItem(stu[1], find);
	if (find)
		stu[1].Print(cout);
}
