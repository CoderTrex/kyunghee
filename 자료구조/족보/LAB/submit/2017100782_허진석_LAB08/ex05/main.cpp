#include <iostream>
#include "UnsortedType.h"

int main()
{
	UnsortedType<int> ul;

	ul.InsertItem(5);
	ul.InsertItem(2);
	ul.InsertItem(3);
	ul.InsertItem(1);
	ul.InsertItem(4);
	ul.InsertItem(6);

	ul.Print();
}
