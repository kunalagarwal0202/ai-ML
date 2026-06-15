
#Binary Search Tree (BST) 

"""Binary Search Tree (BST) is a binary tree where:

Every node has at most two children.
All values in the left subtree are smaller than the node.
All values in the right subtree are greater than the node."""

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    # Insert
    def insert(self, data):

        if self.root is None:
            self.root = Node(data)

        else:
            self._insert(self.root, data)

    def _insert(self, node, data):

        if data < node.data:

            if node.left is None:
                node.left = Node(data)

            else:
                self._insert(node.left, data)

        elif data > node.data:

            if node.right is None:
                node.right = Node(data)

            else:
                self._insert(node.right, data)

    # Search
    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):

        if node is None:
            return False

        if node.data == data:
            return True

        if data < node.data:
            return self._search(node.left, data)

        return self._search(node.right, data)

    # Inorder Traversal
    def inorder(self):
        self._inorder(self.root)

    def _inorder(self, node):

        if node:

            self._inorder(node.left)

            print(node.data, end=" ")

            self._inorder(node.right)

bst = BST()

bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder Traversal:")
bst.inorder()

print("\n")

print("Search 40:", bst.search(40))
print("Search 100:", bst.search(100))