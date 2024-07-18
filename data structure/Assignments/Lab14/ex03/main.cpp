#include <iostream>
#include "Student.h"
using namespace std;

int main()
{
    Student stu[10];
    Student* stu_Ptrs[10];
    
    stu[1].InitValue(2003200100, (char*)"Ford", 3.3);
    stu[0].InitValue(2004200121, (char*)"smith", 3.0);
    stu[2].InitValue(2005200132, (char*)"donald", 2.7);
    
    for (int k = 0; k < 3; k++){
        stu_Ptrs[k] = &stu[k];
    }
    SelectionSort(stu_Ptrs, 3);
    Print(cout, stu, 3);
    return 0;
}