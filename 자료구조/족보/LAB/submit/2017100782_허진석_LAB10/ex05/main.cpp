#include "UnsortedType.h"
#include "TreeType.h"
#include <iostream>

bool MatchingItemUnsorted(TreeType &tree, UnsortedType<ItemType> &list) {
	int list_len = list.LengthIs();
	int tree_len = tree.LengthIs();

	if (list_len != tree_len)
		return false;
	else {
		ItemType item;
		bool found;
		list.ResetList();
		for (int i = 0; i < list_len; i++) {
			list.GetNextItem(item);
			tree.RetrieveItem(item, found);
			if (!found)
				return false;
		}
		return true;
	}
}

int main(void) {
	TreeType t;
	t.InsertItem(10);
	t.InsertItem(20);
	UnsortedType<int> u;
	u.InsertItem(10);
	u.InsertItem(30);
	std::cout << MatchingItemUnsorted(t, u) << std::endl;
}
