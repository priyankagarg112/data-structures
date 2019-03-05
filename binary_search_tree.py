class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.rec_insert(data, self.root)

    def rec_insert(self, data, curr):
        if data > curr.data:
            if curr.right == None:
                curr.right = Node(data)
            else:
                self.rec_insert(data, curr.right)
        elif data < curr.data:
            if curr.left == None:
                curr.left = Node(data)
            else:
                self.rec_insert(data, curr.left)
        else:
            print(f"{data} already exists in tree.")

    def display_tree(self):
        if self.root != None:
            self.rec_display(self.root)
        else:
            print("Tree is empty.")

    def rec_display(self, curr):
        if curr !=None:
            self.rec_display(curr.left)
            print(curr.data)
            self.rec_display(curr.right)


bst = BinarySearchTree()
from random import randint
for _ in range(49):
    data = randint(0,500)
    bst.insert(data)
bst.display_tree()
