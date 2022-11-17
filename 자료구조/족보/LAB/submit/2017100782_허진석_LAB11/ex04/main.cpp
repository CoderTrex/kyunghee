#include <iostream>
#include "StackType.h"

/*
A. 최우선순위 원소는 무엇인가?
	Time-Stamp가 가장 큰 원소로 가장 나중에 들어온 원소이다.
B. 4장에 있는 명세서를 이용하여 Push와 Pop 알고리즘을 작성하여라
C. 4장에서 구현된 Push, Pop 연산과 위의 두 연산을 Big-O 개념으로 비교하여라.
	4장의 Push와 Pop 산의 시간복잡도는 O(1)인 반면, Priority Queue 기반의 Stack은 O(logN)이다.
	둘다, 메모리 공간이 정해져있기 때문에 PQ 기반의 Stack은 큰 이점은 없어 보인다.
*/

int main() {
	StackType s;

	s.Push(1);
	s.Push(4);
	s.Push(3);
	s.Push(7);
	s.Push(8);
	s.Push(10);
	s.Push(6);

	while (!s.IsEmpty()) {
		int top = s.Top();
		std::cout << top << " ";
		s.Pop();
	}
	std::cout << '\n';
}
