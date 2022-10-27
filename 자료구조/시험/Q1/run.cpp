#include <iostream>
#include "StrType.h"
using namespace std;

int main() {
    StrType Str01("ABCD");
    StrType Str02("EFG");

    Str01.Print();
    Str02.Print();

    Str01.Concat(Str02);

    Str01.Print();
}
