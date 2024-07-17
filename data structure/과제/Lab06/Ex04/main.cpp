#include "UnsortedType.h"
#include <stdlib.h>
#include <time.h>
using namespace std;


int main() {
	UnsortedType<int> list;
	
	
	list.InsertItem(50);
	list.InsertItem(3);
	list.InsertItem(4);
	list.InsertItem(37);
	list.InsertItem(35);
	list.InsertItem(3);
	list.InsertItem(3);
	list.InsertItem(3);
	list.InsertItem(3);
	list.InsertItem(20);
	list.InsertItem(18);
	list.InsertItem(21);
	// "B를 제대로 구현하면 A를 구현하는 것과 같은 이치이므로 A를 따로 구현하지 않는다\n";
	cout << "Origin List\n";
	list.Print();

	cout << "Delete num 4\n";
	list.DeleteItem(4);
	list.Print();
	cout << "Delete num 100\n";
	list.DeleteItem(100);
	list.Print();
	cout << "Delete num 3\n";
	list.DeleteItem(3);
	list.Print();
}