#include "Student.h"
#include <string.h>

void Print(ostream& out, Student stu[], int numelement)
{
	for(int i=0; i<numelement; i++)
	{
		stu[i].Print(out);
	}
}
void Student::Print(ostream &out)
{
	out << id << "\t" << name << "\t" << gpa << endl;
}
void Student::InitValue(int _id, char *_name, float _gpa)
{
	id = _id;
	strncpy(name, _name, sizeof(name));
	gpa = _gpa;
}
void Student::getValue(int &_id, char *_name, float &_gpa)
{
	_id = id;
	strncpy(_name, name, sizeof(name));
	_gpa = gpa;
}
char *Student::getName()
{
	return name;
}
void Student::operator = (Student stu)
{
	id = stu.id;
	strncpy(name, stu.name, sizeof(name));
	gpa = stu.gpa;
}
bool Student::operator < (const Student &stu)
{
	if (id != stu.id)
		return id < stu.id;
	int res = strcmp(name, stu.name);
	if (res != 0)
	{
		if (res == 1)
			return false;
		else
			return true;
	}
	return gpa < stu.gpa;
}
bool Student::operator <= (const Student &stu)
{
	if (id != stu.id)
		return id < stu.id;
	int res = strcmp(name, stu.name);
	if (res != 0)
	{
		if (res == 1)
			return false;
		else
			return true;
	}
	return gpa <= stu.gpa;
}
bool Student::operator == (const Student &stu)
{
	return id == stu.id && strcmp(name, stu.name) == 0 && gpa == stu.gpa;
}
void PrintByPointer(ostream &out, Student *values[], int numValues)
{
	for (int i = 0; i < numValues; i++)
	{
		(*values[i]).Print(out);
	}
}

