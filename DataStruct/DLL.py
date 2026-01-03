class node:
    def __init__(self,val):
        self.prev=None
        self.next=None
        self.value=val

    def __str__(self):
        return str(self.value)

class doublyLL:
    def __init__(self,val):
        NewNode= node(val)
        self.head=NewNode
        self.tail=NewNode
        self.len=1

    def append(self, val):
        Newnode= node(val)
        Newnode.next=None
        Newnode.prev=self.tail
        self.tail.next=Newnode
        self.tail=Newnode
        self.len=self.len+1

    def prepend(self, val):
        Newnode= node(val)
        Newnode.next=self.head
        self.head.prev=Newnode
        self.head=Newnode
        self.len=self.len+1


    def trav(self):
        temp=self.head
        for i in  range(0,self.len):
            print(temp)
            temp=temp.next

dll=doublyLL(10)
dll.append(50)
dll.append(60)
dll.append(90)
dll.prepend(-1)
dll.prepend(-2)
dll.trav()