#ifndef STACK_H
#define STACK_H

#include <iostream>
#include "NodeType.h"

class EmptyStack
// Exception class thrown by Pop and Top when stack is emtpy.
{};

template <class ItemType>
class StackType
{
public:
	StackType();
	~StackType();
	bool IsFull() const;
	bool IsEmpty() const;
	void Push(ItemType item);
	void Pop();
	ItemType Top();

private:
	NodeType<ItemType> *topPtr;
};

template <class ItemType>
void StackType<ItemType>::Push(ItemType newItem)
{
	NodeType<ItemType> *location;
	location = new NodeType<ItemType>;
	location->info = newItem;
	location->next = topPtr;
	topPtr = location;
}
template <class ItemType>
void StackType<ItemType>::Pop()
{
	if (IsEmpty())
		throw EmptyStack();
	else
	{
		NodeType<ItemType> *tempPtr;
		tempPtr = topPtr;
		topPtr = topPtr->next;
		delete tempPtr;
	}
}
template <class ItemType>
ItemType StackType<ItemType>::Top()
{
	if (IsEmpty())
		throw EmptyStack();
	else
		return topPtr->info;
}

template <class ItemType>
bool StackType<ItemType>::IsEmpty() const
{
	return (topPtr == NULL);
}
template <class ItemType>
bool StackType<ItemType>::IsFull() const
{
	NodeType<ItemType> *location;
	try
	{
		location = new NodeType<ItemType>;
		delete location;
		return false;
	}
	catch (std::bad_alloc)
	{
		return true;
	}
}

template <class ItemType>
StackType<ItemType>::~StackType()
{
	NodeType<ItemType> *tempPtr;

	while (topPtr != NULL)
	{
		tempPtr = topPtr;
		topPtr = topPtr->next;
		delete tempPtr;
	}
}
template <class ItemType>
StackType<ItemType>::StackType() // Class constructor.
{
	topPtr = NULL;
}

#endif