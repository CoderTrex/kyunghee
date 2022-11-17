// Header file for Unsorted List ADT.
#include <new>
template<class ItemType2>
struct NodeType2;

// Assumption:  ItemType2 is a type for which the operators "<" 
// and "==" are defined-either an appropriate built-in type or
// a class that overloads these operators.

template<class ItemType2>
class SortedType {
public:
	SortedType();     // Class constructor
	~SortedType();    // Class destructor

	bool IsFull() const;
	// Determines whether list is full.
	// Post: Function value = (list is full)

	int LengthIs() const;
	// Determines the number of elements in list.
	// Post: Function value = number of elements in list.

	void MakeEmpty();
	// Initializes list to empty state.
	// Post:  List is empty.

	void RetrieveItem(ItemType2 &item, bool &found);
	// Retrieves list element whose key matches item's key
	// (if present).
	// Pre:  Key member of item is initialized.
	// Post: If there is an element someItem whose key matches
	//       item's key, then found = true and item is a copy
	//       of someItem; otherwise found = false and item is
	//       unchanged.
	//       List is unchanged.

	void InsertItem(ItemType2 item);
	// Adds item to list.
	// Pre:  List is not full.
	//       item is not in list.
	// Post: item is in list.

	void DeleteItem(ItemType2 item);
	// Deletes the element whose key matches item's key.
	// Pre:  Key member of item is initialized.
	//       One and only one element in list has a key matching
	//       item's key.
	// Post: No element in list has a key matching item's key.

	void ResetList();
	// Initializes current position for an iteration through the
	// list.
	// Post: Current position is prior to list.

	void GetNextItem(ItemType2 &);
	// Gets the next element in list.
	// Pre:  Current position is defined.
	//       Element at current position is not last in list.
	// Post: Current position is updated to next position.
	//       item is a copy of element at current position.

private:
	NodeType2<ItemType2> *listData;
	int length;
	NodeType2<ItemType2> *currentPos;
};

template<class ItemType2>
struct NodeType2 {
	ItemType2 info;
	NodeType2 *next;
};

template<class ItemType2>
SortedType<ItemType2>::SortedType()  // Class constructor
{
	length = 0;
	listData = NULL;
}

template<class ItemType2>
bool SortedType<ItemType2>::IsFull() const
// Returns true if there is no room for another ItemType2 
//  on the free store; false otherwise.
{
	NodeType2<ItemType2> *location;
	try {
		location = new NodeType2<ItemType2>;
		delete location;
		return false;
	}
	catch (std::bad_alloc exception) {
		return true;
	}
}

template<class ItemType2>
int SortedType<ItemType2>::LengthIs() const
// Post: Number of items in the list is returned.
{
	return length;
}

template<class ItemType2>
void SortedType<ItemType2>::MakeEmpty()
// Post: List is empty; all items have been deallocated.
{
	NodeType2<ItemType2> *tempPtr;

	while (listData != NULL) {
		tempPtr = listData;
		listData = listData->next;
		delete tempPtr;
	}
	length = 0;
}

template<class ItemType2>
void SortedType<ItemType2>::RetrieveItem(ItemType2 &item,
                                         bool &found) {
	bool moreToSearch;
	NodeType2<ItemType2> *location;

	location = listData;
	found = false;
	moreToSearch = (location != NULL);

	while (moreToSearch && !found) {
		if (location->info < item) {
			location = location->next;
			moreToSearch = (location != NULL);
		}
		else if (item == location->info) {
			found = true;
			item = location->info;
		}
		else
			moreToSearch = false;
	}
}

template<class ItemType2>
void SortedType<ItemType2>::InsertItem(ItemType2 item) {
	NodeType2<ItemType2> *newNode;  // pointer to node being inserted
	NodeType2<ItemType2> *predLoc;  // trailing pointer
	NodeType2<ItemType2> *location; // traveling pointer
	bool moreToSearch;

	location = listData;
	predLoc = NULL;
	moreToSearch = (location != NULL);

	// Find insertion point.
	while (moreToSearch) {
		if (location->info < item) {
			predLoc = location;
			location = location->next;
			moreToSearch = (location != NULL);
		}
		else
			moreToSearch = false;
	}

	// Prepare node for insertion
	newNode = new NodeType2<ItemType2>;
	newNode->info = item;
	// Insert node into list.
	if (predLoc == NULL)         // Insert as first
	{
		newNode->next = listData;
		listData = newNode;
	}
	else {
		newNode->next = location;
		predLoc->next = newNode;
	}
	length++;
}

template<class ItemType2>
void SortedType<ItemType2>::DeleteItem(ItemType2 item)
// Pre:  item's key has been initialized.
//       An element in the list has a key that matches item's.
// Post: No element in the list has a key that matches item's.
{
	NodeType2<ItemType2> *location = listData;
	NodeType2<ItemType2> *tempLocation;

	// Locate node to be deleted.
	if (item == listData->info) {
		tempLocation = location;
		listData = listData->next;        // Delete first node.
	}
	else {
		while (!(item == (location->next)->info))
			location = location->next;

		// Delete node at location->next
		tempLocation = location->next;
		location->next = (location->next)->next;
	}
	delete tempLocation;
	length--;
}

template<class ItemType2>

void SortedType<ItemType2>::ResetList()
// Post: Current position has been initialized.
{
	currentPos = NULL;
}

template<class ItemType2>
void SortedType<ItemType2>::GetNextItem(ItemType2 &item)
// Post:  Current position has been updated; item is 
//        current item.
{
	if (currentPos == NULL)
		currentPos = listData;
	item = currentPos->info;
	currentPos = currentPos->next;

}

template<class ItemType2>
SortedType<ItemType2>::~SortedType()
// Post: List is empty; all items have been deallocated.
{
	NodeType2<ItemType2> *tempPtr;

	while (listData != NULL) {
		tempPtr = listData;
		listData = listData->next;
		delete tempPtr;
	}
}
