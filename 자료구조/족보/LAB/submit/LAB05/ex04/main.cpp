#include <iostream>
#include "QueType.h"

void Move(QueType *dst, QueType *src) {
	dst->MakeEmpty();
	while (!src->IsEmpty()) {
		int item;

		src->Dequeue(item);
		dst->Enqueue(item);
	}
	delete src;
	src = NULL;
}

int Length(QueType &queue) {
	int len = 0;
	QueType *tmp = new QueType;

	while (!queue.IsEmpty()) {
		int item;

		queue.Dequeue(item);
		tmp->Enqueue(item);
		len++;
	}
	Move(&queue, tmp);
	return len;
}

int main() {
	QueType q1, q2;
	std::cout << Length(q1) << " ";
	std::cout << q2.Length() << std::endl;
	for (int i = 0; i < 10; i++) {
		q1.Enqueue(i);
		q2.Enqueue(i);

		std::cout << Length(q1) << " ";
		std::cout << q2.Length() << std::endl;
	}

	while (!q2.IsEmpty()) {
		int item;

		q2.Dequeue(item);
		std::cout << q2.Length() << " ";
	}
	std::cout << "\n";
}