#include "SelectionSort.h"
#include <iostream>

template <class ItemType>
int MinIndex(ItemType values[], int startIndex, int endIndex)
// Post: Returns the index of the smallest value in
//       values[startIndex]..values[endIndex].
{
	int indexOfMin = startIndex;
	for (int index = startIndex + 1; index <= endIndex; index++)
		if (values[index] < values[indexOfMin])
			indexOfMin = index;
	return indexOfMin;
}

template <class ItemType>
void SelectionSort(ItemType values[], int numValues)
// Post: The elements in the array values are sorted by key.
{
	int endIndex = numValues - 1;
	for (int current = 0; current < endIndex; current++)
		Swap(values[current],
			 values[MinIndex(values, current, endIndex)]);
}

void SelectionSort(Student ary[], int numElems)
{
	// Selection Sort 구현하기
	int indexOfMin = numElems - 1;
	for (int i = 0; i < numElems - 1; i++)
		Swap(ary[i], ary[MinIndex(ary, i, numElems - 1)]);
}
