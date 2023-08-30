class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, node = None):
        self.root = node
    
    def preorder(self, root):
        if root != None:
            print(root.data, end=' ')
            if root.left:
                self.preorder(root.left)
            if root.right:
                self.preorder(root.right)

    def inorder(self, root):
        if root != None:
            if root.left:
                self.inorder(root.left)
            print(root.data, end=' ')
            if root.right:
                self.inorder(root.right)

    def postorder(self, root):
        if root != None:
            if root.left:
                self.postorder(root.left)
            if root.right:
                self.postorder(root.right)
            print(root.data, end=' ')


BT = BinaryTree()
N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(4)
N5 = Node(5)
N6 = Node(6)
N7 = Node(7)
N8 = Node(8)

BT.root = N1
N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.left = N6
N3.right = N7
N4.left = N8

BT.preorder(N1)
print()
BT.inorder(N1)
print()
BT.postorder(N1)
