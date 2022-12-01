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
    stu[0].InitValue(2003200111, "leewoongjae", 3.0);
    stu[1].InitValue(2004200121, "kwonojong", 3.2);
    stu[2].InitValue(2005200132, "kimjinli", 2.7);

    SelectionSort(stu, 3);
    Print(cout, stu, 3);
    return 0;
}