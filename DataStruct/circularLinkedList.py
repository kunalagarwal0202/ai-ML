class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class circularLinkedList:
    def __init__(self,value):
        New_Node=Node(value)
        New_Node.next=New_Node
        self.tail=New_Node
        self.head=New_Node
        self.length=1

    def append(self, value):
        New_node=Node(value)
        New_node.next=self.head
        self.tail.next=New_node
        self.tail=New_node
    
    def prepend(self,value):
        NewNode= Node(value)
        NewNode.next=self.head
        self.head =NewNode
        self.tail.next=NewNode

    def insert(self, pos, val):
        temp=self.head
        for i in range(0,pos-1):
            temp=temp.next
        newNode= Node(val)
        newNode.next=temp.next
        temp.next=newNode
    
    def get(self, index):

        temp=self.head
        for i in range(index):
            temp=temp.next
        print(temp.value)


    def remove (self,index):
        if index==0:
            self.head=self.head.next
            self.tail.next=self.head
        else:
            temp=self.head
            for i in range(index-1):
                temp=temp.next
            popped_node=temp.next
            temp.next=temp.next.next


       
        


    def pri(self):
        temp= self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
            if temp ==self.head:
                break
class main:
    cll= circularLinkedList(10)
    cll.append(8)
    cll.append(9)
    cll.append(3)
    cll.prepend(0)
    cll.prepend(77)
    cll.insert(4,99)

    cll.pri()
    cll.remove(4)
    cll.pri()


