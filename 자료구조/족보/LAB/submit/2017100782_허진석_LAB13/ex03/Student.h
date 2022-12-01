#ifndef _STUDENT_H
#define _STUDENT_H

#include <iostream>
#include <cstring>

using namespace std;

class Student
{
public :
	void Print(ostream& out);
	void InitValue(int _id, char* _name, float _gpa);
	void getValue(int& _id, char* _name, float& _gpa);
	char* getName();
	void operator = (Student stu);
	bool operator<(const Student &s)
	{
		if (id != s.id)
			return id < s.id;
		int res = strcmp(name, s.name);
		if (res != 0)
		{
			if (res == 1)
				return false;
			else
				return true;
		}
		return gpa < s.gpa;
	}
	bool operator>(const Student &s)
	{
		if (id != s.id)
			return id > s.id;
		int res = strcmp(name, s.name);
		if (res != 0)
		{
			if (res == 1)
				return true;
			else
				return false;
		}
		return gpa > s.gpa;
	}

private :
	int id;
	char name[30];
	float gpa;
};

void Swap(Student& item1, Student& item2);
void Print(ostream& out, Student stu[], int numelement);
void PrintByPointer(ostream& out, Student* values[], int numValues);

#endif