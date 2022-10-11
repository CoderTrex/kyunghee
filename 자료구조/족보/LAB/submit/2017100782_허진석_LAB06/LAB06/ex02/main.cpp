#include "QueType.h"

void ReplaceItem(QueType<int> &queue, int oldItem, int newItem) {
	QueType<int> temp_queue; //백업용 스택
	int temp_Item; // top을 받는 아이템
	while(!queue.IsEmpty())
	{
		queue.Dequeue(temp_Item);
		if(temp_Item == oldItem) {
			temp_queue.Enqueue(newItem);
		}else{
			temp_queue.Enqueue(temp_Item);
		}
	}
	while(!temp_queue.IsEmpty()) {
		temp_queue.Dequeue(temp_Item);
		queue.Enqueue(temp_Item);
	}
}

int main() {
	QueType<int> q;
	for (int i = 0; i < 10; i++) {
		q.Enqueue(i);
	}
	std::cout << "Before replacing\n";
	q.Print();
	// q.ReplaceItem(4, 100);
	ReplaceItem(q, 4, 100);
	std::cout << "After replacing\n";
	q.Print();
}