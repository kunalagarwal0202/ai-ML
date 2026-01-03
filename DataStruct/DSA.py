print("test")


class node:
    def __init__(self, value):
        self.value=value
        self.next=None
class linkedlist:
    def __init__(self,value):
        newnode=node(value)
        self.head=newnode
        self.tail=newnode
        self.length=1

    def insertAtEnd(self, value):
        newnode=node(value)
        newnode.next=None
        self.tail.next=newnode
        self.tail=newnode
        self.length=self.length+1

    def insertAtBegin(self, value):
        new_node= node(value)
        new_node.next=self.head
        self.head=new_node
        self.length=self.length+1

    def insertAtMiddle(self, value, pos):
        newnode=node(value)
        tempNode=self.head
        for _ in range(pos-1):
            tempNode=tempNode.next
        newnode.next=tempNode.next
        tempNode.next=newnode

    def search(self, value):
        temp= self.head
        for i in range(0,self.length):
            if(temp.value==value):
                print("found at index" , i)
            temp=temp.next

    def print(self):
        temp=self.head
        for i in range(0,self.length):
            print("->" ,temp.value)
            temp=temp.next

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
 
    # if node to be removed is the head node
        elif index == 0:
            popped_node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node
 
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
    
            popped_node = temp.next
        
            # if node to be removed is the tail node
            if popped_node.next is None:
                self.tail = temp
            print("xx", temp.value)

            temp.next = temp.next.next

            print(temp.next)
            popped_node.next = None
            self.length -= 1
            return popped_node
    
    def reversse(self):
        temp=self.head
        self.tail=self.head
        prevNode=None
        nextNode=temp
        curr=temp
        while (nextNode !=None) :
            nextNode=nextNode.next
            curr.next=prevNode
            prevNode=curr
            curr=nextNode
        self.head=prevNode
        

        


    def rev(self):
        curr=self.head
        nextNode=self.head
        prevNode=None

        while(curr!=None):
            nextNode=nextNode.next
            curr.next=prevNode
            prevNode=curr
            curr=nextNode
        self.head=prevNode
    
    def revrecursion(self, temp):

        if(temp ==None or temp.next==None):
            return temp
        
        newHead=self.revrecursion(temp.next)
        front = temp.next
        front.next=temp
        #temp.next=None
        
        return newHead
    
    def revrec(self, head):

        if(head.next ==None):
            return head
        
        newhead= self.revrec(head.next)
        front = head.next
        front.next=head
        #head.next=None

        return newhead
    

    
newlinkedlist=linkedlist(8)
newlinkedlist.insertAtEnd(202)
newlinkedlist.insertAtEnd(2)
newlinkedlist.insertAtEnd(0)
newlinkedlist.insertAtEnd(10)
newlinkedlist.insertAtEnd(230)



#newlinkedlist.print()


    


newlinkedlist.head=newlinkedlist.revrec(newlinkedlist.head)
newlinkedlist.print()

