from itertools import count
import re
from tkinter.messagebox import NO


class TreeNode:

    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f'{self.info}'
    
class BST():

    def __init__(self):
        self.root = None
        self.order_list = []
        self.tmp = None
    
    def is_empty(self):
        return (self.root == None)
    
    def count_nodes(self, tree):
        if tree is None:
            return 0
        else:
            return self.count_nodes(tree.left) + self.count_nodes(tree.right) + 1
		
    def length_is(self):
        return self.count_nodes(self.root)

    def insert(self, item):
        if self.root is None:
            self.root = TreeNode(item)
        else:
            self.insert_item(self.root, item)

    def insert_item(self, node, item):
        if item < node.info:
            if node.left is None:
                node.left = TreeNode(item)
                return
            self.insert_item(node.left, item)
        else:
            if node.right is None:
                node.right = TreeNode(item)
                return
            self.insert_item(node.right, item)
        
  
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            self.order_list.append(node.info)
            self.inorder(node.right)
    
    def preorder(self, node):
        if node is not None:
            self.order_list.append(node.info)
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            self.order_list.append(node.info)

    def delete(self, item):
        self.delete_node(self.root, item)
    
    def delete_node(self, current, item):
        if item < current.info:
            self.tmp = current
            self.delete_node(current.left, item)
        elif item > current.info:
            self.tmp = current
            self.delete_node(current.right, item)
        else:
            tmp = current
            if current.left is None:
                if self.tmp != None:
                    if self.tmp.right == item:
                        self.tmp.right = current.right
                    else:
                        self.tmp.left = current.right
                del tmp
                self.tmp = None
            elif current.right is None:
                if self.tmp != None:
                    if self.tmp.right == item:
                        self.tmp.right = current.left
                    else:
                        self.tmp.left = current.left
                del tmp
                self.tmp = None
            else:
                current.info = self.get_predecessor(current.left)
                self.delete_node(current.left, current.info)

    def get_predecessor(tree):
        while tree.right is not None:
            tree = tree.right
        return tree.info
