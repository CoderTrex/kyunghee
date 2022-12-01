#include <iostream>

template <class ItemType>
void Swap(ItemType &item1, ItemType &item2)
{
	ItemType tempItem;

	tempItem = item1;
	item1 = item2;
	item2 = tempItem;
}

template <class ItemType>
void PrintArr(ItemType arr[], int n)
{
	for (int i = 0; i < n; i++)
		std::cout << arr[i] << " ";
	std::cout << '\n';
}

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
void HeapSort(ItemType values[], int numElems)
{
	int index;

	PrintArr(values, numElems);
	for (index = numElems / 2 - 1; index >= 0; index--)
		ReheapDown(values, index, numElems - 1);

	PrintArr(values, numElems);
	for (index = numElems - 1; index >= 1; index--)
	{
		Swap(values[0], values[index]);
		ReheapDown(values, 0, index - 1);
		PrintArr(values, numElems);
	}
}
