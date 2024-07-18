#pragma once
#include <iostream>
using namespace std;


template <class ItemType>
void Swap(ItemType &item1, ItemType &item2)
{
	ItemType tempItem;

	tempItem = item1;
	item1 = item2;
	item2 = tempItem;
}

template <class ItemType>
void Print_array(ItemType value[], int numValue)
{
	for (int i = 0; i < numValue; i++)
	{
		cout << value[i] << " ";
	}
	cout << "\n";
}

template<class ItemType>
void ReheapDown(ItemType elements[], int root, int bottom)
// Post: Heap property is restored.
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

template<class ItemType>
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

template<class ItemType>
void HeapSort(ItemType values[], int numValues) {
	int index;

	Print_array(values, numValues);
	// Convert the array of values into a heap.
	for (index = numValues/2 - 1; index >= 0; index--)
		ReheapDown(values, index, numValues-1);
	Print_array(values, numValues);
	// Sort the array.
	for (index = numValues-1; index >=1; index--)
	{
		Swap(values[0], values[index]);
		ReheapDown(values, 0, index-1);
		Print_array(values, numValues);
	}
}