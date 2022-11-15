#include "SortedType.h"
#include "TreeType.h"
#include <iostream>

void AddElement(TreeType &tree, int arr[], int from, int to);
void MakeTree(TreeType &tree, SortedType<int> &list);

int main(void) {
	TreeType t;
	SortedType<int> l;
	for (int i = 0; i < 10; i++) {
		l.InsertItem(i);
	}
	MakeTree(t, l);
}

void AddElement(TreeType &tree, int arr[], int from, int to) {
	int mid;
	if (from < to) {
		mid = (from + to) / 2;
		tree.InsertItem(arr[mid]);
		AddElement(tree, arr, from, mid - 1);
		AddElement(tree, arr, mid + 1, to);
	}
}

void MakeTree(TreeType &tree, SortedType<int> &list) {
	int len = list.LengthIs();
	int *arr = new int[len];
	int item_info;
	int i;
	list.ResetList();
	for (i = 0; i < len; i++) {
		list.GetNextItem(item_info);
		arr[i] = item_info;
	}
	AddElement(tree, arr, 0, len - 1);
	delete [] arr;
}
