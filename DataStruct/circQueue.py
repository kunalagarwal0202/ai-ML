class queue:
    def __init__(self, maxsize):
        self.items=[None]*maxsize
        self.maxsize=maxsize
        self.start=-1
        self.top=-1
    def __str__(self):
        values =[str(x) for x in self.items]
        return ' '.join(values)
    def isFull(self):
        if(self.top+1==self.start):
            return True
        if(self.start==0 and self.top==self.maxsize):
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top ==-1:
            return True
        else:
            return False
        
    def enqueue(self, value):
        if (self.isFull()):
            return "queue full bhai"
        else:
            if(self.top+1==self.maxsize):
                self.top=0
            else:
                self.top=self.top+1
                if self.start==-1:
                    self.start=0
            self.items[self.top]=value
            return "Element added at the end"
        
    def dequeue(self):
        if(self.isEmpty()):
            return "queue is empty cannot dequeue"
        else:
            start=self.start
            if self.start==self.top:
                self.start=-1
                self.top=-1
            if self.start+1==self.maxsize:
                self.start=0
            else:
                self.start =self.start+1
            self.items[start]=None
           
        

test =queue(10)
test.enqueue(1)
test.enqueue(2)
test.enqueue(3)
test.enqueue(4)
test.enqueue(5)
test.enqueue(6)
test.enqueue(7)
test.enqueue(8)
test.enqueue(9)
test.enqueue(10)
test.dequeue()
test.dequeue()
test.dequeue()
test.dequeue()
test.dequeue()
test.dequeue()
test.enqueue(11)



class node:
    def __init__(self,val):
        self.value=val
        self.next=None

class sll:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def append(self,val):
        print('in append')
        newNode= node(val)
        temp=self.head
        if(self.size==0):
            self.head=newNode
            self.tail=newNode
            self.size=1
        else:
            self.tail.next=newNode
            self.tail=newNode
            self.size=self.size+1
    def prin(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    def remove(self):
        self.head=self.head.next
        self.size=self.size-1


newQueue=sll()
newQueue.append(1)
newQueue.append(2)
newQueue.append(3)
newQueue.append(4)
newQueue.append(5)
newQueue.remove()
newQueue.prin()

print(newQueue.size)

print("----")
int(2)

def fib(n):
    if n in [0,1]:
        return n
    else:
        res=(fib(n-1)+fib(n-2))
        return res
print(fib(9))

        
