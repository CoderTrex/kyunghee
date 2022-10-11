#include "SortedType.h"
#include <stdlib.h>
#include <time.h>
using namespace std;


int main() {
	SortedType<int> list;

	for (int i = 20; i > 0; i--) {
		list.InsertItem(i);
	}
	list.InsertItem(1);
	list.InsertItem(1);
	cout << "Origin List\n";
	list.Print();

	cout << "Delete num 1\n";
	list.DeleteItem(1);
	list.Print();
	cout << "Delete num 50\n";
	list.DeleteItem(50);
	list.Print();
	cout << "Delete num 7\n";
	list.DeleteItem(7);
	list.Print();
}