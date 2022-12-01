#pragma once
#include "Student.h"

template <class ItemType>
void ReheapDown(ItemType elements[], int root, int bottom)
{
	int maxChild;
	int rightChild;
	int leftChild;

	leftChild = root * 2 + 1;
	rightChild = root * 2 + 2;
	if (leftChild <= bottom)
	{
		if (leftChild == bottom)
			maxChild = leftChild;
		else
		{
			if (elements[leftChild] <= elements[rightChild])
				maxChild = rightChild;
			else
				maxChild = leftChild;
		}
		if (elements[root] < elements[maxChild])
		{
			Swap(elements[root], elements[maxChild]);
			ReheapDown(elements, maxChild, bottom);
		}
	}
}

template <class ItemType>
void ReheapUp(ItemType elements[], int root, int bottom)
// Post: Heap property is restored.
{
	int parent;

	if (bottom > root)
	{
		parent = (bottom - 1) / 2;
		if (elements[parent] < elements[bottom])
		{
			Swap(elements[parent], elements[bottom]);
			ReheapUp(elements, root, parent);
		}
	}
}

void HeapSort(Student ary[], int numElems)
{
	int index;
	for (index = numElems/2 - 1; index >= 0; index--)
		ReheapDown(ary, index, numElems - 1);
	for (index = numElems - 1; index >= 1; index--)
	{
		Swap(ary[0], ary[index]);
		ReheapDown(ary, 0, index - 1);
	}
}
