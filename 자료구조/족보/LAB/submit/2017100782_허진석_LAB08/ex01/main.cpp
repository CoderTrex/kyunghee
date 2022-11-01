#include "UnsortedType.h"

int main()
{
	UnsortedType<int> ul;

	for (int i = 0; i < 5; i++)
		ul.InsertItem(i);

	ul.PrintSumSquares();
}
