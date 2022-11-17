#include "PQType.h"
#include <iostream>

/*
A. 위의 힙에 다음과 같은 연산을 수행시킨 결과를 보여라.
	pq.Enqueue(28);
	pq.Enqueue(2);
	pq.Enqueue(40);
	pq.Dequeue(x);
	pq.Dequeue(y);
	pq.Dequeue(z);
B. (A)번 문제의 연산을 수행하고 난 이후에는 x, y, z가 어떤 값이 되는가?
	각각 56, 42, 40
*/

int main() {
	using namespace std;

	PQType<int> pq(50);

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

	cout << x << " " << y << " " << z << endl;
}