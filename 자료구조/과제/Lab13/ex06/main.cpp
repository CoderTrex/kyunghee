#include <iostream>
#include "Student.h"
#include "HeapSort.h"
using namespace std;

int main()
{
    Student stu[100];
    stu[0].InitValue(2003200111, (char *)"leewoongjae", 3.0);
    stu[1].InitValue(2004200121, (char *)"kwonojong", 3.2);
    stu[2].InitValue(2005200142, (char *)"kimjinli", 2.7);
    stu[3].InitValue(2006200152, (char *)"eiowieoi", 2.3);
    stu[4].InitValue(2007200172, (char *)"dfjknli", 2.0);
    stu[5].InitValue(2008200182, (char *)"hehkii", 1.7);
    stu[6].InitValue(2009200232, (char *)"eunjeong", 3.7);
    stu[7].InitValue(2010200262, (char *)"kimhaseung", 4.0);

    GetHeightSum(stu, 8);
    HeapSort(stu, 8);
    Print(cout, stu, 8);
    return 0;
}