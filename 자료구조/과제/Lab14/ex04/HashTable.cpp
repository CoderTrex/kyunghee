#include  "Student.h"

const int MAX_ITEMS = 20000;

template<class ItemType>
class HashTable{
public:
    HashTable(){}
    HashTable(ItemType emptyKey);
    int Hash(char *key) const;
    void RetrieveItem(ItemType& item, bool& found);
    void InsertItem(ItemType item);
private:
    ItemType info[MAX_ITEMS];
    ItemType emptyItem;
    int length;
};

int getintfromstring(char *key)
{
    int sum = 0;
    int len = strlen(key);
    if (len % 2 == 1) len++;
    for (int j = 0; j < len; j++)
        sum  = sum + key[j] * 100 + key[j + 1];
    return sum;
}

template<class ItemType>
int HashTable<ItemType>::Hash(char *key) const
{
    return (getIntFromString(key) % MAX_ITEMS);
}

template<class ItemType>
void HashTable<ItemType>::InsertItem(ItemType item)
{
    int location;
    location = Hash(item.getKey());
    while (info[location] != emptyItem)
        location = (location + 1) % MAX_ITEMS;
    info[location] = item;
    length++;
}

template<class ItemType>
void HashTable<ItemType>::RetrieveItem(ItemType &item, bool &found)
{
    int location;
    int startLoc;
    bool moreTosearch = true;

    startLoc = Hash(item.getkey());
    location = startLoc;
    do {
        if (info[location == item] || info[location] == emptyItem)
            moreTosearch = false;
        else
            location = (location + 1) % MAX_ITEMS
    } while (moreTosearch && location);
    found = (info[location] == item);
    if (found)
        item  = info[location];
}