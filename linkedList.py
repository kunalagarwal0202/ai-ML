# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        # If list is empty
        if self.head is None:
            self.head = new_node
            return

        # Traverse till last node
        temp = self.head

        while temp.next:
            temp = temp.next
            new_node.next

        temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Delete a node
    def delete(self, key):
        # If head itself contains key
        temp=self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None

        while temp and temp.data != key:
            prev = temp 
            temp = temp.next 

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next
        temp = None


# Creating linked list
ll = LinkedList()

# Inserting elements
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.insert(50)
ll.insert(60)
ll.insert(70)
ll.insert(80)
ll.insert(90)
ll.insert(100)

# Display list
print("Linked List:")
ll.display()

# Delete node
ll.delete(20)

print("After Deletion:")
ll.display()