// heap은 자식들이 왼쪽 오른쪽에 어떤 수가 들어가도 상관 없음
// 다만 아래로 내려갈 수록 작은 수이다. 위로 올라갈수록 높은 수이다.
// 왼쪽에 자신보다 작은 값 오른쪽에 큰 값이라는 조건이 없음
#include <iostream>
#include <algorithm>
#include <stdlib.h>

template<class ItemType>
struct HeapType
{
    void ReheapDown(int root, int bottom);
    void ReheapUp(int root, int bottom);

    ItemType *elements;
    int numElement;
};

template<class ItemType>
void HeapType<ItemType>::ReheapDown(int root, int bottom)
{
    int maxChild;
    int rightChild;
    int leftChild;

    leftChild = root * 2 + 1;
    rightChild = root * 2 + 2;

    if (leftChild <= bottom)
    {
        if (leftChild == bottom)
            maxChild = leftChild;
        else
        {
            if (elements[leftChild] <= elements[rightChild])
                maxChild = rightChild;
            else
                maxChild = leftChild;
        }
    }
    if (elements[root] < elements[maxChild])
    {
        Swap(elements[root], elements[maxChild]);
        ReheapDown(maxChild, bottom);
    }
}

template<class Itemtype>
void HeapType<Itemtype>::ReheapUp(int root, int bottom)
{
    int parent;

    if (bottom > root)
    {
        parent = (bottom-1)/2;
        if (elements[parent] < elements[bottom])
        {
            Swap(elements[parent], element[bottom]);
            ReheapUp(root, parent);
        }
    }
}