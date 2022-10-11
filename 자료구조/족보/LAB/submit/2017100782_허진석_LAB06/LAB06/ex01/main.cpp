#include "StackType.h"

void ReplaceItem(StackType &stack, ItemType oldItem, ItemType newItem) {
	StackType temp_stack; //백업용 스택
	ItemType temp_Item; // top을 받는 아이템
	while(!stack.IsEmpty())
	{
		temp_Item = stack.Top();
		if(temp_Item == oldItem) {
			temp_stack.Push(newItem);
		}else{
			temp_stack.Push(stack.Top());
		}
		stack.Pop();
	}
	while(!temp_stack.IsEmpty()) {
		stack.Push(temp_stack.Top());
		temp_stack.Pop();
	}
}

int main() {
	StackType s;
	for (int i = 0; i < 10; i++) {
		s.Push(i);
	}
	std::cout << "Before replacing\n";
	s.Print();
	std::cout << "After replacing\n";
	s.ReplaceItem(4, 100);
	ReplaceItem(s, 4, 100);
	s.Print();
}