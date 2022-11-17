template <class ItemType>
void swap(ItemType& one, ItemType& two);

template<class ItemType>
// Assumes ItemType is either a built-in simple type or a class
// with overloaded relational operators.
struct HeapType
{
  void ReheapDown(int root, int bottom);
  void ReheapUp(int root, int bottom);
  ItemType* elements;   // Array to be allocated dynamically
  int numElements;
};

template <class ItemType>
void Swap(ItemType& one, ItemType& two)
{
  ItemType temp;
  temp = one;
  one = two;
  two = temp;
}  

// recursive 방식 :
template<class ItemType>
void HeapType<ItemType>::ReheapUp(int root, int bottom)
// Post: Heap property is restored.
{
  int parent;
  
  if (bottom > root)
  {
    parent = (bottom-1) / 2;
    if (elements[parent] < elements[bottom])
    {
      Swap(elements[parent], elements[bottom]);
      ReheapUp(root, parent);
    }
  }
}

// nonorecursive 방식 :
template<class ItemType>
void HeapType<ItemType>::ReheapUp(int root, int bottom)
// Post: Heap property is restored.
{
  int parent;
  while (bottom > root)
  {
    parent = (bottom-1)/2;
    if (elements[parent] < elements[bottom])
        swap(elements[parent], elements[bottom]);
    bottom = parent;
  }
}

// recursive version 
template<class ItemType>
void HeapType<ItemType>::ReheapDown(int root, int bottom)
// Post: Heap property is restored.
{
  int maxChild;
  int rightChild;
  int leftChild;

  leftChild = root*2+1;
  rightChild = root*2+2;
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
    if (elements[root] < elements[maxChild])
    {
      Swap(elements[root], elements[maxChild]);
      ReheapDown(maxChild, bottom);
    }
  }
}

// nonrecursion version:
template<class ItemType>
void HeapType<ItemType>::ReheapDown(int root, int bottom)
// root 노드를 제외하고 나머지 노드들은 heap의 조건을 만족하고 있음
{
  int maxChild, leftChild, rightChild;
  bool reheaped = false; // root가 제 위치를 찾아가 reheap이 되면 True
  leftChild = root * 2 + 1; // root 값으로부터 왼쪽 자식노드의 위치 계산
  while(leftChild <= bottom && !reheaped)
  {
    if(leftChild == bottom) // 왼쪽 자식 노드 하나만 있는 경우
      maxChild = leftChild;
    else{
      rightChild = root * 2 + 2;
      maxChild = (elements[leftChild] <= elements[rightChild]) ? : ;
    }
    if(elements[root] < elements[maxChild]) {
      Swap(elements[root], elements[maxChild]);
      root = maxChild; // maxChild 가 root의 새로운 위치가 됨
      leftChild = root;
    }
    else
      reheaped = true;
  }
}

