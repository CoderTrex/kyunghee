#ifndef _STUDENT_H
#define _STUDENT_H

#include <iostream>
#include <cstring>

using namespace std;

class Student
{
public:
	Student(): id(0), gpa(0.0) {};
	void Print(ostream &out);
	void InitValue(int _id, char *_name, float _gpa);
	void getValue(int &_id, char *_name, float &_gpa);
	char *getName();
	char *getKey();
	void operator=(Student stu);
	bool operator==(const Student &s)
	{
		return id == s.id && strcmp(name, s.name) == 0 && gpa == s.gpa;
	}
	bool operator!=(const Student &s)
	{
		return id != s.id || strcmp(name, s.name) != 0 || gpa != s.gpa;
	}

private:
	int id;
	char name[30];
	float gpa;
};

void Swap(Student &item1, Student &item2);
void Print(ostream &out, Student stu[], int numelement);
void PrintByPointer(ostream &out, Student *values[], int numValues);

#endif