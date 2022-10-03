#include "QueType.h"

QueType::QueType(int max)
// Parameterized class constructor
// Post: maxQue, front, and rear have been initialized.
//       The array to hold the queue elements has been dynamically
//       allocated.
{
  maxQue = max + 1;
  front = maxQue - 1;
  rear = maxQue - 1;
  minus_pos = -1;
  min_pos = front;
  items = new ItemType[maxQue];
}

QueType::QueType()          // Default class constructor
// Post: maxQue, front, and rear have been initialized.
//       The array to hold the queue elements has been dynamically
//       allocated.
{
  maxQue = 501;
  front = maxQue - 1;
  rear = maxQue - 1;
  minus_pos = -1;
  min_pos = front;
  items = new ItemType[maxQue];
}

QueType::~QueType()         // Class destructor
{
  delete [] items;
}

void QueType::MakeEmpty()
// Post: front and rear have been reset to the empty state.
{
  front = maxQue - 1;
  rear = maxQue - 1;
}

bool QueType::IsEmpty() const
// Returns true if the queue is empty; false otherwise.
{
  return (rear == front);
}

bool QueType::IsFull() const
// Returns true if the queue is full; false otherwise.
{
  return ((rear + 1) % maxQue == front);
}

void QueType::Enqueue(ItemType newItem)
// Post: If (queue is not full) newItem is at the rear of the queue;
//       otherwise a FullQueue exception is thrown.  
{
  if (IsFull())
    throw FullQueue();
  else if (minus_pos != -1)
    items[minus_pos] = newItem;
  else
  {
    rear = (rear + 1) % maxQue;
    items[rear] = newItem;
  }
  FindMin();
}

void QueType::Dequeue(ItemType& item)
// Post: If (queue is not empty) the front of the queue has been 
//       removed and a copy returned in item; 
//       othersiwe a EmptyQueue exception has been thrown.
{
  if (IsEmpty())
    throw EmptyQueue();
  else
  {
    front = (front + 1) % maxQue;
    item = items[front];
  }
}

void QueType::MinDeque(ItemType& item)
{
  if (IsEmpty())
    throw EmptyQueue();
  else
  {
    item = items[min_pos];
    items[min_pos] = -1;
    minus_pos = min_pos;
    FindMin();
  }
}

void QueType::FindMin()
{
  int min = 2147483647;
  for (int i = (front + 1) % maxQue; i < (rear + 1) % maxQue; i++)
  {
    if (i != min_pos && items[i] != -1 && items[i] < min)
    {
      min_pos = i;
      min = items[i];
    }
  }
}
