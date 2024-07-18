// 시간 복잡도 시험에 나옴 꼬고 공부하기
#include "HeapType.c++"

// class FullPQ() {};
// class Empty() {};

template<class Itemtype>
class PQType
{
public:
    PQType(int);
    ~PQType();
    void MakeEmpty();
    bool IsEmpty() const;
    bool IsFull() const;
    void Enqueue(Itemtype newItem);
    void Dequeue(Itemtype &item);
private:
    int length;
    HeapType<Itemtype> items;
    int maxItem;
}

