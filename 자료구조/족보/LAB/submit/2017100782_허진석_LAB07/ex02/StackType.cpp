#include <cstddef>
#include <new>
#include <iostream>
#include "StackType.h"

void StackType::Push(ItemType newItem)
{
	if (IsFull())
		throw FullStack();
	else
	{
		NodeType *location;
		location = new NodeType;
		location->info = newItem;
		location->next = topPtr;
		topPtr = location;
	}
}
void StackType::Pop()
{
	if (IsEmpty())
		throw EmptyStack();
	else
	{
		NodeType *tempPtr;
		tempPtr = topPtr;
		topPtr = topPtr->next;
		delete tempPtr;
	}
}
ItemType StackType::Top()
{
	if (IsEmpty())
		throw EmptyStack();
	else
		return topPtr->info;
}
bool StackType::IsEmpty() const
{
	return (topPtr == NULL);
}

void StackType::MakeEmpty()
{
	NodeType *tempPtr;

	while (topPtr != NULL)
	{
		tempPtr = topPtr;
		topPtr = topPtr->next;
		delete tempPtr;
	}
}

bool StackType::IsFull() const
{
	NodeType *location;
	try
	{
		location = new NodeType;
		delete location;
		return false;
	}
	catch (std::bad_alloc)
	{
		return true;
	}
}

StackType::~StackType()
{
	MakeEmpty();
}

StackType::StackType() // Class constructor.
{
	topPtr = NULL;
}

void StackType::Copy(StackType& anotherStack) const
{
	StackType tmp;
	NodeType *tmpNode = topPtr;
	
	anotherStack.MakeEmpty();

	while (tmpNode != NULL) {
		tmp.Push(tmpNode->info);
		tmpNode = tmpNode->next;
	}
	while (!tmp.IsEmpty()) {
		anotherStack.Push(tmp.Top());
		tmp.Pop();
	}
}

void StackType::Print()
{
	NodeType *tmp = topPtr;
	while (tmp != NULL)
	{
		std::cout << tmp->info << " ";
		tmp = tmp->next;
	}
	std::cout << std::endl;
}

StackType& StackType::operator= (const StackType& anotherStack) {
	anotherStack.Copy(*this);

	return (*this);
}
