

#Double linked list

class DLList:
    def __init__(self):
        self.head = None

    def find_tail(self):
        last=self.head
        while last.next:
            last = last.next
        return last

    def add(self, data):
        if not self.head:
            self.head = DLNode
            return True

        tail = self.find_tail()

        new_node = DLNode(data)
        tail.next = new_node
        new_node.prev =tail
        return True

    def insert_after(self, prev_node, data):
        #this method inserts data AFTER prev_node
        prev_node is a doubly linked, which means it's prev pointer has to point to  
        to its previous node and it's next pointer has to point to the next node in the list.
        





















class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        
class DLNode(Node):
    def __init__(self, data):
        self.prev = None
        super().__init__(data)

class LinkedList:
    def __init__(self):
        self


    

