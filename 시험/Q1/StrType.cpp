#include <iostream>
#include <cstddef>
#include <stdlib.h>
#include "StrType.h"
using namespace std;

StrType::StrType(const char *inp){
	Node *location;
	location = new Node;
	int i = 0;
	while (inp[i]){
		char newword = inp[i];
		location->ch = newword;
		location->next = str;
		str = location;
		i++;
	}
	
}

void StrType::MakeEmpty()
{
	str = NULL;
}

int	StrType::LengthIs()
{
	int	l = 0;

	Node	*t;
	t = str;
	while(t != NULL) {
		l++;
		t = t->next;
	}
	return l;
}

void StrType::Print()
{
	Node	*t;

	t = str;

	while(t != NULL) {
		std::cout << t->ch;
		t = t->next;

	}
	std::cout << '\n';
}

int	StrType::Compare(StrType &o)
{
	int	diff;
	Node	*t1, *t2;

	t1 = str;
	t2 = o.str;
	while(t1 != NULL) {
		diff = t1->ch - t2->ch;
		if(diff != 0) return diff;
		t1 = t1->next;
		t2 = t2->next;
	}
	return 0;
}

void StrType::Concat(StrType &o){
	int	diff;
	Node	*t1, *t2;

	t1 = str;
	t2 = o.str;
	while(t1 != NULL) {
		t1 = t1->next;
	}
	while (t2 != NULL){
		t1->ch = t2->ch;
		t1 = t1->next;
		t2 = t2->next; 
	}
}
