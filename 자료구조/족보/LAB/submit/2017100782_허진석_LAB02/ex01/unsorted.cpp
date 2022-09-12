// Implementation file for Unsorted.h

#include "unsorted.h"
UnsortedType::UnsortedType()
{
  length = 0;
}
bool UnsortedType::IsFull() const
{
  return (length == MAX_ITEMS);
}

int UnsortedType::LengthIs() const
{
  return length;
}
void UnsortedType::RetrieveItem(ItemType& item, bool& found) 
// Pre:  Key member(s) of item is initialized. 
// Post: If found, item's key matches an element's key in the 
//       list and a copy of that element has been stored in item; 
//       otherwise, item is unchanged. 
{
  bool moreToSearch;
  int location = 0;
  found = false;

  moreToSearch = (location < length);

  while (moreToSearch && !found) 
  {
    switch (item.ComparedTo(info[location]))
    {
      case LESS    : 
      case GREATER : location++;
                     moreToSearch = (location < length);
                     break;
      case EQUAL   : found = true;
                     item = info[location];
                     break;
    }
  }
}
void UnsortedType::InsertItem(ItemType item)
// Post: item is in the list.
{
  info[length] = item;
  length++;
}
void UnsortedType::DeleteItem(ItemType item)
// Pre:  item's key has been initialized.
//       An element in the list has a key that matches item's.
// Post: No element in the list has a key that matches item's.
{
  int location = 0;

  while (item.ComparedTo(info[location]) != EQUAL)
    location++;

  info[location] = info[length - 1];
  length--;
}
void UnsortedType::DeleteItem_a(ItemType item)
// Pre:  List has been initialized.
//       Key member of item is initialized.
// Post: No element in list has a key matching item's key.
{
  int loc = 0;
  while (loc < length) {
    if (item.ComparedTo(info[loc]) == EQUAL) {
      if (loc == length - 1)
        length--;
      else
        info[loc] = info[--length];
      return;
    }
    loc++;
  }
}
void UnsortedType::DeleteItem_c(ItemType item)
// Pre:  List has been initialized.
//       Key member of item is initialized.
// Post: No element in list has a key matching item's key.
{
  int loc = 0;
  this->Print();
  while (loc < length) {
    if (item.ComparedTo(info[loc]) == EQUAL) {
      while (length >= 0 && item.ComparedTo(info[loc]) == EQUAL) {
        if (loc == length - 1) {
          length--;
          return;
        }
        else
          info[loc] = info[--length];
      }
    }
    loc++;
  }
}
void UnsortedType::ResetList()
// Post: currentPos has been initialized.
{
  currentPos = -1;
}

void UnsortedType::GetNextItem(ItemType& item)
// Post: item is current item.
//       Current position has been updated.
{
  currentPos++;
  item = info[currentPos];
}
