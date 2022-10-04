#include <iostream>
#include <cstdlib>
#include <ctime>
#include "QueType.h"

#define MAX_SIZE 10

int gen_rand() {
	return rand() % 100;
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

	srand((unsigned int)time(NULL));
	for(int i = 0; i < MAX_SIZE; i++) {
		int item = gen_rand();
		q.Enqueue(item);
	}
	print_queue(q);
}
