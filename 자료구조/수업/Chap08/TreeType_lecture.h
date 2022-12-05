#include <string.h>
#include <fstream>
#include "QueType.h"

typedef char ItemType;
struct TreeNode;

enum OrderType {PRE_ORDER, IN_ORDER, POST_ORDER};

int imp_SingleParnetCount(TreeNode *tree);

template<class ItemType>
class TreeType{
public:
    TreeType();
    ~TreeType();
    TreeType(const TreeType<ItemType>);
    void operator=(const TreeType &originalTree);
    void MakeEmpty();
    bool IsEmpty() const;
    bool IsFull() const;
    int LengthIs() const;
    void RetrieveItem(ItemType&, bool& found); 
    void InsertItem(ItemType);
    void DeleteItem(ItemType);
    void ResetTree(OrderType);
    void GetNextItem(ItemType&, OrderType, bool&); 
    void PrintTree(ofstream&) const;
private:
    TreeNode *root;
    QueType preQue;
    QueType inQue;
    QueType postQue;
};
