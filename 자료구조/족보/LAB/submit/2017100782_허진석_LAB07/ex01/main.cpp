#include "SortedType.h"

int main() {
	SortedType<int> sl;

	for (int i = 0; i < 20; i++) {
		sl.InsertItem(i);
	}
	sl.PrintReverse();
}
