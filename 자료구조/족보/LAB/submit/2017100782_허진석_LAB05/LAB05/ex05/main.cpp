#include <iostream>
#include "QueType.h"

void move(QueType *dst, QueType *src) {
	dst->MakeEmpty();
	while (!src->IsEmpty()) {
		int item;

		src->Dequeue(item);
		dst->Enqueue(item);
	}
	delete src;
	src = NULL;
}

void print_queue(QueType &q) {
	QueType *tmp = new QueType;

	while (!q.IsEmpty()) {
		int item;

		q.Dequeue(item);
		tmp->Enqueue(item);
		std::cout << item << " ";
	}
	std::cout << "\n";
	move(&q, tmp);
}


int main() {
	QueType q1;

	for (int i = 0; i < 15; i++) {
		q1.Enqueue(i);
	}
	print_queue(q1);
	std::cout << "===========================\n";
	while (!q1.IsEmpty()) {
		int item;

		q1.Dequeue(item);
		print_queue(q1);
	}
}
	