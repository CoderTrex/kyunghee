#include "Student.h"

template <class ItemType>
void InsertItem(ItemType values[], int startIndex, int endIndex)
{
	bool finished = false;
	int current = endIndex;
	bool moreToSearch = (current != startIndex);

	while (moreToSearch && !finished)
	{
		if (values[current] < values[current - 1])
		{
			Swap(values[current], values[current - 1]);
			current--;
			moreToSearch = (current != startIndex);
		}
		else
			finished = true;
	}
}

void InsertionSort(Student ary[], int numElems)
{
	for (int count = 0; count < numElems; count++)
		InsertItem(ary, 0, count);
}
