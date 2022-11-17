#include <iostream>
#include "PQType.h"

/*
A.PQType의 정의는 어떻게 변경되어야 하는가?
	생성자의 파라미터가 void로 변경된다.
B. 연결리스트로 구현하는 Enqueue 연산을 작성하여라.
C. 연결리스트로 구현하는 Dequeue 연산을 작성하여라.
D. 위의 두 Enqueue와 Dequeue 연산을 Heap의 연산과 비교하라 (Big-O 개념)
	Heap 기반의 Priority Queue는 Enqueue, Dequeue 모두 O(logN)의 시간복잡도를 갖지만, 
	LinkedList 기반의 Priority Queue는 O(N)의 시간복잡도를 갖는다.
*/

void test() {
	PQLLType<int> pq;

	int arr[] = {
		56, 27, 42, 26, 15, 3, 19, 25, 24, 5, 28, 2, 40
	};
	for (int i = 0; i < 13; i++) {
		pq.Enqueue(arr[i]);
	}
	int x, y, z;
	pq.Dequeue(x);
	pq.Dequeue(y);
	pq.Dequeue(z);
	std::cout << x << " " << y << " " << z << '\n';
}

int main() {
	test();
	system("leaks a.out");
}