#include "StackType.h"
#include <iostream>

StackType::StackType()
{
	pq = new PQType<StackNode>(100);
	length = 0;
}

StackType::~StackType()
{
	delete pq;
}

bool StackType::IsEmpty() const
{
	return pq->IsEmpty();
}

bool StackType::IsFull() const
{
	return pq->IsFull();
}

void StackType::Push(ItemType newItem)
{
	StackNode new_node;
	new_node.info = newItem;
	new_node.time_stamp = length++;
	pq->Enqueue(new_node);
}

void StackType::Pop()
{
	if (IsEmpty())
		throw EmptyStack();
	StackNode i;

	pq->Dequeue(i);
	length--;
}

ItemType StackType::Top()
{
	StackNode i;
	ItemType data;

	pq->Dequeue(i);
	data = i.info;
	pq->Enqueue(i);
	return data;
}
