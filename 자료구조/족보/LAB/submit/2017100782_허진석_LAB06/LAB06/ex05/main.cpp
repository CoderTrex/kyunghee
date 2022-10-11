#include "SortedType.h"

int main() {
	SortedType<int> s;

	for (int i = 0; i < 20; i++) {
		s.InsertItem(i);
	}
	s.InsertItem(5);
	s.InsertItem(5);
	s.InsertItem(5);
	s.InsertItem(5);
	s.InsertItem(5);
	std::cout << "Origin\n";
	s.Print();
	std::cout << "Delete no item test (item: 32)\n";
	s.DeleteItem(32);
	s.Print();
	std::cout << "Delete a item test (item: 10)\n";
	s.DeleteItem(10);
	s.Print();
	std::cout << "Delete all item test (item: 5)\n";
	s.DeleteAllItems(5);
	s.Print();
}