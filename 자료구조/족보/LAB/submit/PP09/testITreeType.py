from ITreeType import IterBST

if __name__ == '__main__':

    tree = IterBST()
    tree.insert(5)
    tree.insert(2)
    tree.insert(3)
    tree.insert(1)
    tree.insert(9)
    tree.insert(8)
    tree.insert(7)
 

    print("Inorder Result")
    tree.inorder(tree.root)
    print(tree.order_list)
    tree.order_list.clear()
    print("\nPreorder Result")
    tree.preorder(tree.root)
    print(tree.order_list)
    tree.order_list.clear()
    print("\nPostorder Result")
    tree.postorder(tree.root)
    print(tree.order_list)
    tree.order_list.clear()
    print()

    print("Delete Result")
    tree.delete(1)
    tree.delete(8)
    tree.inorder(tree.root)
    print(tree.order_list)
    tree.order_list.clear()
    
