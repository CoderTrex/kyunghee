#include <iostream>
#include "LILIST.h"

LILIST::LILIST()
{
	elem = NULL;
}

LILIST::~LILIST()
{
	Node *iter = elem;
	Node *target;

	while (iter != nullptr)
	{
		target = iter;
		iter = iter->next;
		delete target;
		target = nullptr;
	}
}

int LILIST::isLength(void)
{
	int length;
	Node *t;

	length = 0;
	t = elem;
	while (t != NULL)
	{
		length++;
		t = t->next;
	}
	return length;
}

void LILIST::InsertList(char *clist)
{
	int i, j;
	char str[100];
	Node *list, *node, *t;

	list = NULL;
	i = 0;
	i++; // skip (
	// Make a linked list
	LILIST *ll = new LILIST;
	node = new Node;
	do
	{
		j = 0;
		while (isdigit(clist[i]))
			str[j++] = clist[i++];
		str[j] = '\0';
		while (isspace(clist[i]))
			++i;
		ll->InsertItem(atoi(str));
	} while (clist[i] != ')');
	
	t = elem;
	while (t->next != nullptr)
		t = t->next;
	node->next = nullptr;
	node->item = -1;
	node->sublist = ll->elem;
	t->next = node;
}

void LILIST::InsertItem(int v)
{
	int size = isLength();
	Node *last = elem;
	Node *new_node = new Node;

	new_node->item = v;
	new_node->sublist = nullptr;
	new_node->next = nullptr;

	if (elem == nullptr)
	{
		elem = new_node;
		return;
	}
	for (int i = 0; i < size - 1; i++)
		last = last->next;
	last->next = new_node;
}

void LILIST::DeleteItem(int v)
{
	Node *t = elem;
	Node *target = nullptr;

	if (t == nullptr)
		return;
	else if (t->item == v)
	{
		elem = t->next;
		target = t;
		t = t->next;
		delete target;
		target = nullptr;
	}

	while (t->next != nullptr)
	{
		if (t->next->item == v)
		{
			target = t->next;
			t->next = t->next->next;
		}
		t = t->next;
		if (target != nullptr)
		{
			delete target;
			target = nullptr;
		}
	}
}

int LILIST::Sum1()
{
	Node *iter = elem;
	int res = 0;

	while (iter != nullptr)
	{
		if (iter->sublist == nullptr)
			res += iter->item;
		iter = iter->next;
	}
	return res;
}

int LILIST::Sum2()
{
	Node *iter = elem;
	Node *iter2;
	int res = 0;

	while (iter != nullptr)
	{
		if (iter->sublist == nullptr)
			res += iter->item;
		else
		{
			iter2 = iter->sublist;
			while (iter2 != nullptr)
			{
				res += iter2->item;
				iter2 = iter2->next;
			}
		}
		iter = iter->next;
	}
	return res;
}

void LILIST::PrintRec(Node *t)
{
	while (t != NULL)
	{
		if (t->sublist != NULL)
		{
			std::cout << "(";
			PrintRec(t->sublist);
			std::cout << ") ";
		}
		else
			std::cout << t->item << " ";
		t = t->next;
	}
	std::cout << "\b";
}

void LILIST::Print()
{
	std::cout << "Content: (";
	PrintRec(elem);
	std::cout << ")\n";
}
