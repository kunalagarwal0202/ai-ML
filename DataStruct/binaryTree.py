class treeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

    def preOrder(self,node):
        if(node is None):
            return
        print(node.data)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def preOrderSearch(self,node, val):
        if(node is None):
            return
        if node.data == val:
            return"susccses"
        else:    
            self.preOrderSearch(node.left,val)
            self.preOrderSearch(node.right,val)
            return "not found"

    def inOrder(self,node):
        if(node is None):
            return
        self.inOrder(node.left)
        print(node.data)
        self.inOrder(node.right)

    def postOrder(self,node):
        if(node is None):
            return
        self.inOrder(node.left)
        self.inOrder(node.right)
        print(node.data)
        

newtree=treeNode(5)
leftNode=treeNode(7)
rightNode=treeNode(8)
leftNodeLeft=treeNode(6)
leftNodeRight=treeNode(10)
rightNodeLeft=treeNode(77)
rightNodeRight=treeNode(6)

newtree.left=leftNode
newtree.right=rightNode
leftNode.left=leftNodeLeft
leftNode.right=leftNodeRight
rightNode.left=rightNodeLeft
rightNode.right=rightNodeRight

print(newtree.preOrderSearch(newtree,6))
print("-----")
newtree.inOrder(newtree)