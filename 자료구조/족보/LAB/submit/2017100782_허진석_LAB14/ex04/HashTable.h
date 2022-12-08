#ifndef __HASH_H__
#define __HASH_H__

#include "Student.h"

const int MAX_ITEMS = 20000;

int getIntFromString(char *key)
{
	int sum = 0;
	int len = strlen(key);
	if (len % 2 == 1)
		len++;
	for (int j = 0; j < len; j += 2)
		sum = (sum + 100 * key[j] + key[j + 1]) % 19937;
	return sum;
}

template <typename ItemType>
class HashTable
{
public:
	HashTable(): HashTable(Student()) {};
	HashTable(ItemType emptyKey);
	int Hash(char *key) const;
	void RetrieveItem(ItemType &item, bool &found);
	void InsertItem(ItemType item);

private:
	ItemType info[MAX_ITEMS];
	ItemType emptyItem;
	int length;
};

template <typename ItemType>
HashTable<ItemType>::HashTable(ItemType emptyKey)
{
	emptyItem = emptyKey;
	for (int i = 0; i < MAX_ITEMS; i++)
		info[i] = emptyItem;
	length = 0;
}

template <typename ItemType>
int HashTable<ItemType>::Hash(char *key) const
{
	return (getIntFromString(key) % MAX_ITEMS);
}

template <typename ItemType>
void HashTable<ItemType>::InsertItem(ItemType item)
{
	int loc;
	loc = Hash(item.getKey());
	while (info[loc] != emptyItem)
		loc = (loc + 1) % MAX_ITEMS;
	info[loc] = item;
	length++;
}

template <typename ItemType>
void HashTable<ItemType>::RetrieveItem(ItemType &item, bool &found)
{
	int loc;
	int startLoc;
	bool moreToSearch = true;
	startLoc = Hash(item.getKey());
	loc = startLoc;
	do
	{
		if (info[loc] == item || info[loc] == emptyItem)
			moreToSearch = false;
		else
			loc = (loc + 1) % MAX_ITEMS;
	} while (moreToSearch && loc);
	found = (info[loc] == item);
	if (found)
		item = info[loc];
}

#endif //__HASH_H__
