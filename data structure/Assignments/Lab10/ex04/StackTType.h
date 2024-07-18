
#include <iostream>
using namespace std;
// The class definition for StackType using templates 
class FullStack
{};
// Exception class thrown by Push when stack is full.

class EmptyStack
// Exception class thrown by Pop and Top when stack is emtpy.
{};

#include "MaxItem.h"
#include <cstdlib>
#include <time.h>
// MaxItems.h must be provided by the user of this class.
// This file must contains the definition of MAX_ITEMS,
// themaximum number ofitems on the stack.

template<class ItemType>		
class StackType
{
public:

    StackType();
    // Class constructor.
    bool IsFull() const;
    // Function: Determines whether the stack is full.
    // Pre:  Stack has been initialized.
    // Post: Function value = (stack is full)
    bool IsEmpty() const;
    // Function: Determines whether the stack is empty.
    // Pre:  Stack has been initialized.
    // Post: Function value = (stack is empty)
    void Push(ItemType item, int rand);
    // Function: Adds newItem to the top of the stack.
    // Pre:  Stack has been initialized.
    // Post: If (stack is full), FullStack exception is thrown;
    //       otherwise, newItem is at the top of the stack.
    void Pop();
    // Function: Removes top item from the stack.
    // Pre:  Stack has been initialized.
    // Post: If (stack is empty), EmptyStack exception is thrown;
    //       otherwise, top element has been removed from stack.
    ItemType Top();
    // Function: Returns a copy of top item on the stack.
    // Pre:  Stack has been initialized.
    // Post: If (stack is empty), EmptyStack exception is thrown;
    //       otherwise, top element has been removed from stack.
    ItemType print();
           
private:
    int top;
    ItemType  items[MAX_ITEMS];	
    ItemType  priority[MAX_ITEMS];
    int Time_Stamp = 0;
};


// The function definitions for class StackType.

// The function definitions for class StackType.
template<class ItemType>
StackType<ItemType>::StackType()
{
  top = -1;
}

template<class ItemType>
bool StackType<ItemType>::IsEmpty() const
{
  return (top == -1);
}

template<class ItemType>
bool StackType<ItemType>::IsFull() const
{
  return (top == MAX_ITEMS-1);
}

template<class ItemType>
void StackType<ItemType>::Push(ItemType newItem, int rand) 
{
  srand((unsigned int)time(NULL));
  static int num = 10;

  if (IsFull()) 
    FullStack();
  top++;
  items[top] = newItem;
  num = rand;
  priority[top] = num;
}

template<class ItemType>
void StackType<ItemType>::Pop()
{
  if( IsEmpty() )
    EmptyStack();
  int max_index = 0, max_num = 0;
  int len = top;
  while (len > -1)
  {
    if (priority[len] > max_num)
    {
      max_num = priority[len];
      max_index = len;
    }
    len--;
  }
  items[max_index] = items[top];
  priority[max_index] = priority[top];
  top--;
}

template<class ItemType>
ItemType StackType<ItemType>::Top()
{
  if (IsEmpty())
    EmptyStack();
  return items[top];
}  

template<class Itemtype>
Itemtype StackType<Itemtype>::print()
{
  int len = top;
  while (len > -1)
  {
    cout << items[len] << " " << priority[len] << "\n";
    len--;
  }
}