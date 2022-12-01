#include "Student.h"

template <class ItemType>
void BubbleDown(ItemType values[], int startIndex, int endIndex)
{
	for (int index = endIndex; index > startIndex; index--)
		if (values[index] < values[index - 1])
			Swap(values[index], values[index - 1]);
}

void BubbleSort(Student ary[], int numElems)
{
	int current = 0;

	while (current < numElems - 1)
	{
		BubbleDown(ary, current, numElems - 1);
		current++;
	}
}
