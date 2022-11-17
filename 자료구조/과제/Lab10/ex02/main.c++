#include "PQType.h"
#include <iostream>
using namespace std;


int main()
{
    PQType<int> pqueue(50);

    pqueue.Enqueue(56);
    pqueue.Enqueue(27);
    pqueue.Enqueue(42);
    pqueue.Enqueue(26);
    pqueue.Enqueue(15);
    pqueue.Enqueue(3);
    pqueue.Enqueue(19);
    pqueue.Enqueue(25);
    pqueue.Enqueue(24);
    pqueue.Enqueue(5);

    pqueue.Enqueue(28);
    pqueue.Enqueue(2);
    pqueue.Enqueue(40);
    int x, y, z;
    
    pqueue.Dequeue(x);
    pqueue.Dequeue(y);
    pqueue.Dequeue(z);

    cout << "x:" << x << " y:" << y << " z:" << z << endl;
}

// 예상한 결과는 간단하게 생각 없이 queue로 생각해서 56, 27, 42로 생각을 했다.
// 하지만 이는 pqueue였기 때문에 element가 큰 순서인 56, 42, 40 순서대로 출력이된다.
// 이는 reheapdown이에서 최대값을 반환하기 때문이다.