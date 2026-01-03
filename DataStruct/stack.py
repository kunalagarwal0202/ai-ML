class stack:

    def __init__(self):
        self.items=[]
        self.len=0

    def push(self, val):
        self.len=self.len+1
        self.items.append(val)


myStack= stack()
