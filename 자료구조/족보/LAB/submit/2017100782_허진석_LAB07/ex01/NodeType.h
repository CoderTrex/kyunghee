#ifndef NODE_H
#define NODE_H

template <class ItemType>
struct NodeType;

template <class ItemType>
struct NodeType
{
	ItemType info;
	NodeType *next;
};

#endif