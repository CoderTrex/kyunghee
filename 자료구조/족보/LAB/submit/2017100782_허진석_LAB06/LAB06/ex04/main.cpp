#include "UnsortedType.h"

int main() {
	UnsortedType<int> u1;
	for (int i = 0; i < 20; i++) {
		u1.InsertItem(i);
	}
	u1.InsertItem(5);
	u1.InsertItem(5);
	u1.InsertItem(5);
	u1.InsertItem(5);
	u1.InsertItem(5);
	std::cout << "Origin List\n";
	u1.Print();
	std::cout << "Delete no item test (item: 32)\n";
	u1.DeleteItem(32);
	u1.Print();
	std::cout << "Delete a item test (item: 10)\n";
	u1.DeleteItem(10);
	u1.Print();
	std::cout << "Delete all item test\n";
	std::cout << "Before\n";
	u1.Print();
	std::cout << "After\n";
	u1.DeleteAllItem(5);
	u1.Print();
}