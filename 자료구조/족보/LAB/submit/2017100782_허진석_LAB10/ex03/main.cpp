#include "TreeType.h"
#include <iostream>

int Smaller(TreeType tree, int value) {
	ItemType item;
	bool finished = false;
	int count = 0;
	tree.ResetTree(IN_ORDER);
	do {
		tree.GetNextItem(item, IN_ORDER, finished);
		if (item < value)
			count++;
		else
			finished = true;
	} while (!finished);
	return count;
}

int main() {
	TreeType t;
	for (int i = 0; i < 10; i++) {
		t.InsertItem(i);
	}
	std::cout << Smaller(t, 5) << std::endl;
}
