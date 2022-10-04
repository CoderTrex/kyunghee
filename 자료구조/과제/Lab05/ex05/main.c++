#include <iostream>
#include "QueType.h"
using namespace std;

void move(QueType *result, QueType *original) {
	result->MakeEmpty();
	while (!original->IsEmpty()) {
		int item;

		original->Dequeue(item);
		result->Enqueue(item);
	}
	delete original;
	original = NULL;
}

void print_queue(QueType &queue) {
	QueType *tmp = new QueType;

	while (!queue.IsEmpty()) {
		int item;

		queue.Dequeue(item);
		tmp->Enqueue(item);
		cout << item << " ";
	}
	cout << "\n";
	move(&queue, tmp);
}


int main() {
	QueType one;

	for (int i = 0; i < 15; i++) {
		one.Enqueue(i);
	}
	print_queue(one);
	while (!one.IsEmpty()) {
		int item;

		one.Dequeue(item);
		print_queue(one);
	}
}
	