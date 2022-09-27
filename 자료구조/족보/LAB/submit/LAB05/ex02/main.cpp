#include <iostream>
#include "QueType.h"

// For a
void ReplaceItem(QueType &queue, int oldItem, int newItem) {
	QueType temp;

	while (!queue.IsEmpty()) {
		int item;

		queue.Dequeue(item);
		if (item != oldItem) {
			temp.Enqueue(item);
		} else {
			temp.Enqueue(newItem);
		}
	}
	while (!temp.IsEmpty()) {
		int item;

		temp.Dequeue(item);
		queue.Enqueue(item);
	}
}

void print_queue(QueType &q) {
	while (!q.IsEmpty()) {
		int item;

		q.Dequeue(item);
		std::cout << item << " ";
	}
	std::cout << "\n";
}

int main() {
	QueType q;

	for(int i = 0; i < 30; i++) {
		q.Enqueue(i % 5);
	}
	// ReplaceItem(q, 3, 100); for a
	// q.ReplaceItem(3, 100); for b
	std::cout << "After replacing\n";
	print_queue(q);
}
