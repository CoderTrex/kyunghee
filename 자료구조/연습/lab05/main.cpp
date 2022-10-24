#include <iostream>
#include "QueType.h"

int main() {
	QueType q1;
	int item;

	q1.Enqueue(3);
	q1.Enqueue(1);
	q1.Enqueue(2);
	q1.Enqueue(5);
	q1.Enqueue(4);
	q1.Enqueue(8);
	q1.Enqueue(7);
	q1.Enqueue(10);

	q1.MinDeque(item);
	std::cout << "item: " << item << "\n";
	q1.MinDeque(item);
	std::cout << "item: " << item << "\n";
	q1.Enqueue(1);
	q1.MinDeque(item);
	std::cout << "item: " << item << "\n";
	q1.MinDeque(item);
	std::cout << "item: " << item << "\n";
}
