// Definition of class PQType, which represents the Priority Queue ADT
class FullPQ
{
};

class EmptyPQ
{
};

#include "Heap.h"
#include "SortedType.h"

template <class ItemType>
class PQLLType
{
public:
	PQLLType();	 // parameterized class constructor
	~PQLLType(); // class destructor

	void MakeEmpty();
	// Function: Initializes the queue to an empty state.
	// Post: Queue is empty.

	bool IsEmpty() const;
	// Function: Determines whether the queue is empty.
	// Post: Function value = (queue is empty)

	bool IsFull() const;
	// Function: Determines whether the queue is full.
	// Post: Function value = (queue is full)

	void Enqueue(ItemType newItem);
	// Function: Adds newItem to the rear of the queue.
	// Post: if (the priority queue is full) exception FullPQ is thrown;
	//       else newItem is in the queue.

	void Dequeue(ItemType &item);
	// Function: Removes element with highest priority from the queue
	// and returns it in item.
	// Post: If (the priority queue is empty) exception EmptyPQ is thrown;
	//       else highest priority element has been removed from queue.
	//       item is a copy of removed element.
private:
	int length;
	SortedType<ItemType> items;
};

template <class ItemType>
PQLLType<ItemType>::PQLLType()
{
	length = 0;
}

template <class ItemType>
void PQLLType<ItemType>::MakeEmpty()
{
	length = 0;
	items.MakeEmpty();
}

template <class ItemType>
PQLLType<ItemType>::~PQLLType() {}

template <class ItemType>
void PQLLType<ItemType>::Dequeue(ItemType &item)
// Post: element with highest priority has been removed
//       from the queue; a copy is returned in item.
{
	if (length == 0)
		throw EmptyPQ();
	items.ResetList();
	items.GetNextItem(item);
	items.DeleteItem(item);
	length--;
}

template <class ItemType>
void PQLLType<ItemType>::Enqueue(ItemType newItem)
// Post: newItem is in the queue.
{
	if (items.IsFull())
		throw FullPQ();
	items.InsertItem(newItem);
	length++;
}

template <class ItemType>
bool PQLLType<ItemType>::IsFull() const
// Post: Returns true if the queue is full; false, otherwise.
{
	return items.IsFull();
}

template <class ItemType>
bool PQLLType<ItemType>::IsEmpty() const
// Post: Returns true if the queue is empty; false, otherwise.
{
	return length == 0;
}
