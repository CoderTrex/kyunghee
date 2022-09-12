
from lib2to3.pytree import NodePattern
from operator import truediv
from platform import node


class NodeType:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class IterBST():
    def __init__(self):
        self.root = None
        self.order_list = []
        self.tmp = None

    def insert(self, data):
        new_node = NodeType(data)
        node_ptr, parent_ptr = self.find_node(self.root, data)
        if parent_ptr is None:
            self.root = new_node
        elif data < parent_ptr.info:
            parent_ptr.left = new_node
        else:
            parent_ptr.right = new_node

    def find(self, key):
        self.find_node(self.root, key)

    def find_node(self, root, key):
        node_ptr = root
        parent_ptr = None

        while node_ptr != None:
            if key < node_ptr.info:
                parent_ptr = node_ptr
                node_ptr = node_ptr.left
            elif key > node_ptr.info:
                parent_ptr = node_ptr
                node_ptr = node_ptr.right
            else:
                break
        return node_ptr, parent_ptr

    def delete(self, key):
        node_ptr, parent_ptr = self.find_node(self.root, key)
        if node_ptr == self.root:
            self.delete_node(self.root, key)
        else:
            self.tmp = parent_ptr
            if parent_ptr.left == node_ptr:
                self.delete_node(parent_ptr.left, key)
            else:
                self.delete_node(parent_ptr.right, key)

    def delete_node(self, node, key):
        tmp = node
        if node.left is None:
            if self.tmp != None:
                if self.tmp.right == key:
                    self.tmp.right = node.right
                else:
                    self.tmp.left = node.right
            del tmp
            self.tmp = None
        elif node.right is None:
            if self.tmp != None:
                if self.tmp.right == key:
                    self.tmp.right = node.left
                else:
                    self.tmp.left = node.left
            del tmp
            self.tmp = None
        else:
            node.info = self.get_predecessor(node.left)
            self.delete_node(node.left, node.info)
        
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

    def get_predecessor(tree):
        while tree.right is not None:
            tree = tree.right
        return tree.info

