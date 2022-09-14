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

// 첫번째 요구조건 코드 구현 (하나 있으면 하나만 삭제하고 종료)
void UnsortedType::DeleteItem(ItemType item)
// Pre:  item's key has been initialized.
//       An element in the list has a key that matches item's.
// Post: No element in the list has a key that matches item's.
{
  int location = 0;

  while (location < length){
    if (item.ComparedTo(info[location]) != EQUAL){
      location++;
    }
    else{
      if (item.ComparedTo(info[location]) == EQUAL){
        if (location == length -1)
          length--; // 만약 마지막 요소가 해당 요소라면 길이를 줄여서 해당 요소에 접근을 막음
        else
          info[location] = info[--length];
        return ;
      }
    }
  }
}


// 2번째 요구 조건 코드 구현 (삭제할 요소가 뒤에 계속해서 있으면 계속해서 삭제)
void UnsortedType::DeleteItem(ItemType item)
// Pre:  item's key has been initialized.
//       An element in the list has a key that matches item's.
// Post: No element in the list has a key that matches item's.
{
  int location = 0;

  while (location < length){
    if (item.ComparedTo(info[location]) != EQUAL){
      location++;
    }
    else{
      while (length >=0 && item.ComparedTo(info[location]) == EQUAL){
          if (location == length -1){
            --length; // 만약 마지막 요소가 해당 요소라면 길이를 줄여서 해당 요소에 접근을 막음
            return ;
          }
          else
            info[location] = info[--length];
        }
    }
  }
}  /* code */

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
