#include "sorted.h"
#include <iostream>

// 함수: 2개의 정렬 리스트를 합병해서 세 번째 정렬리스트를 만든다.
// 조건: list1과 list2는 초기화되어 있고 ComparedTo라는 함수를 사용해서 키에 의해 정렬되어있다.
// list1과 list2는 같은 킬를 갖지 않는다.
// 결과: 결과는 list1과 list2의 모든 요소를 가진 정렬 리스트이다.
void MergeList(SortedType list1, SortedType list2, SortedType &result) {
	ItemType item1, item2;

	result.ResetList();
	list1.ResetList();
	list2.ResetList();
	for (int i = 0; i < list1.LengthIs(); i++) {
		list1.GetNextItem(item1);
		result.InsertItem(item1);
	}
	for (int i = 0; i < list2.LengthIs(); i++) {
		list2.GetNextItem(item2);
		result.InsertItem(item2);
	}
}

void PrintList(SortedType &list) {
	ItemType item;

	for (int i = 0; i < list.LengthIs(); i++) {
		list.GetNextItem(item);
		item.Print(std::cout);
		std::cout << " ";
	}
	std::cout << "\n";
}

int main() {
	SortedType list1, list2, list3;
	list1.ResetList();
	list2.ResetList();

	ItemType items[20];
	for (int i = 0; i < 20; i++) {
		items[i].Initialize(i + 1);
	}

	for (int i = 0; i < 20; i++) {
		if (i % 2) {
			list1.InsertItem(items[i]);
		}
		else {
			list2.InsertItem(items[i]);
		}
	}
	std::cout << "< LIST_1 >\n";
	PrintList(list1);
	std::cout << "< LIST_2 >\n";
	PrintList(list2);
	MergeList(list1, list2, list3);
	std::cout << "< MERGED LIST >\n";
	PrintList(list3);
}