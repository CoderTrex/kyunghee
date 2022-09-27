#include <iostream>
#include "QueType.h"
#define MAX_SIZE 30

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

// For a
bool Identical(QueType &queue1, QueType &queue2) {
	QueType *tmp1 = new QueType;
	QueType *tmp2 = new QueType;

	while (!queue1.IsEmpty() && !queue2.IsEmpty()) {
		int item1, item2;
		queue1.Dequeue(item1);
		tmp1->Enqueue(item1);
		queue2.Dequeue(item2);
		tmp2->Enqueue(item2);
		if (item1 != item2) {
			Move(&queue1, tmp1);
			Move(&queue2, tmp2);
			return false;
		}
	}
	if (queue1.IsEmpty() && queue2.IsEmpty()) {
		Move(&queue1, tmp1);
		Move(&queue2, tmp2);
		return true;
	}
	Move(&queue1, tmp1);
	Move(&queue2, tmp2);
	return false;
}

int main() {
	QueType q1, q2, q3;

	for(int i = 0; i < 30; i++) {
		q1.Enqueue(i % 5);
		q2.Enqueue(i % 5);
		q3.Enqueue(i % 4);
	}
	// std::cout << Identical(q1, q2) << " ";
	// std::cout << Identical(q1, q3) << "\n";
	std::cout << q1.Identical(q2) << " ";
	std::cout << q1.Identical(q3) << "\n";
}
