#include <iostream>
#include "SelectionSort.h"
#include "Student.h"
#include <string.h>
#include <string>
#include <stdio.h>

using namespace std;

int main()
{
    Student stu[100];
    stu[0].InitValue(2003200111, (char*)"leewoongjae", 3.0);
    stu[1].InitValue(2004200121, (char*)"kwonojong", 3.2);
    stu[2].InitValue(2005200132, (char*)"kimjinli", 2.7);
    stu[3].InitValue(2005200132, (char*)"kikdjinli", 2.7);
    stu[4].InitValue(2005200132, (char*)"dimjinli", 2.7);

    SelectionSort(stu, 5);
    Print(cout, stu, 5);
    return 0;
}