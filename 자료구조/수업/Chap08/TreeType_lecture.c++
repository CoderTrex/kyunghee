#include "TreeType.h"

struct TreeNode
{
    ItemType info;
    TreeNode *left;
    TreeNode *right;
};

void Insert(TreeNode *&tree, ItemType item);
void DeleteNode(TreeNode *&tree);
void GetPredecessor(TreeNode *tree, ItemType &data);

bool TreeType::IsEmpty() const
{
    return root == NULL;
}

void Insert(TreeNode *&tree, ItemType item)
{
    if (tree == NULL)
    {
        tree = new TreeNode;
        tree->right = NULL;
        tree->left = NULL;
        tree->info = item;
    }
    else if (item < tree->info)
        Insert(tree->left, item);
    else
        Insert(tree->right, item);
}


int TreeType::LengthIs() const
{
    return CountNodes(root);
}

void DeleteNode(TreeNode *&tree)
{
    ItemType data;
    TreeNode *tempPtr;

    tempPtr = tree;
    if (tree->left == NULL)
    {
        tree = tree->right;
        delete tempPtr;
    }
    else if (tree->right == NULL)
    {
        tree = tree->left;
        delete tempPtr;
    }
    else
    {
        GetPredecessor(tree->left, data);
        tree->info = data;
        Delete(tree->left, data);
    }
}

void GetPredecessor(TreeNode *tree, ItemType &data)
{
    while (tree->right != NULL)
        tree = tree->right;
    data = tree->info;
}

void Delete(TreeNode *&tree, ItemType item)
{
    if (item < tree->info)
        Delete(tree->left, item);
    else if (item > tree->info)
        Delete(tree->right, item);
    else
        DeleteNode(tree);
}

int imp_SingleParnetCount(TreeNode *tree)
{
    if (tree == nullptr)
        return 0;
    
    if ((tree->left == nullptr && tree->right != nullptr) 
        ||(tree->right == nullptr && tree->left != nullptr))
        return 0;
    else
        return imp_SingleParnetCount(tree->left)  + imp_SingleParnetCount(tree->right);
}

int TreeType::SingleParentCount()
{
    return imp_SingleParnetCount(root);
}

bool TreeType::IsFull() const
{
    TreeNode *location;
    try
    {
        location = new TreeNode;
        delete location;
        return false;
    }
    catch(const std::exception& e)
    {
        return true;
    }
    
}

int CountNodes(TreeNode *tree)
{
    if (tree == NULL)
        return 0;
    else
        return CountNodes(tree->left) + CountNodes(tree->right) + 1;
}

void Retrieve(TreeNode *tree, ItemType &item, bool &found)
{
    if (tree == NULL)
    {
        tree = new TreeNode;
        tree->right = NULL;
        tree->left = NULL;
        tree->info = item;
    }
    else if (item < tree->info)
        Insert(tree->left, item);
    else Insert(tree->right, item);
}
