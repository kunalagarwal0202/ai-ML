class Node:
    def __init__(self, data):
        self.data = data      # Value stored in the node
        self.left = None      # Left child
        self.right = None     # Right child


# Traversal Functions

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Creating the Binary Tree
root = Node(10)

root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(8)

root.right.right = Node(20)

# Tree Structure:
#
#         10
#        /  \
#       5    15
#      / \     \
#     2   8     20
#

print("Inorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)