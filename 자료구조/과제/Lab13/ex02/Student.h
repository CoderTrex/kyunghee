#ifndef _STUDENT_H
#define _STUDENT_H

#include <iostream>
#include <string.h>
#include <string>
#include <stdio.h>
using namespace std;

class Student
{
public :
	void Print(ostream& out);
	void InitValue(int _id, char* _name, float _gpa);
	void getValue(int& _id, char* _name, float& _gpa);
	char* getName();
	void operator = (Student stu);
private :
	int id;
	char name[30];
	float gpa;
};


void Student::InitValue(int _id, char* _name, float _gpa)
{
	id = _id;
	strcpy(name, _name);
	// strcpy_s(name, sizeof(name), _name);
	gpa = _gpa;
}

void Print(ostream& out, Student stu[], int numelement)
{
	for(int i=0; i<numelement; i++)
	{
		stu[i].Print(out);
	}
}

// void Swap(Student& item1, Student& item2);

// void Print(ostream& out, Student stu[], int numelement);
// void PrintByPointer(ostream& out, Student* values[], int numValues);

#endif