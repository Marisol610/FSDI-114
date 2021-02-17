

class Node:
    def __init__(self, data):
        self.data =data
        self.next = None


class DLNode(Node):
    def __init__(self, data):
        self.prev = None
        super().__init__(data)



class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data, prev_node, position= None):

        new_node =Node(data)

        if not self.head:
            self.head = new_node
            return True
        
        if prev_node:
            temp = prev_node.next
            prev_node.next = new_node
            new_node.next = temp
            return True

        if position:
            last= self.find_index(index=position)
            if last == self.head:
                last.next =self.head
                self.head = last
                return True
            return self.add(data, prev_node=last)

        last = self.find_index()
        last.next = new_node
        return True

    def find_index(self, index=None):
        last = self.head
        counter = 0

        while(last.next):
            last= last.nextslot
            if counter == index:
                break
            counter += 1
            return last

    def removeNode(self, target_data): #keep track of the head of our list
        if self.head.data == target_data:
            self.head = self.head.nextslot
            return True

        last = self.head
        
        while last:
            current = last.next
            if current.data = target_data:
                last.next = current.next
                return True

            last = last.next
        return False
              


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
        temp = temp.next
        if(temp == Null)
        {
            return False
        }
    pointer.data= new_node
    pointer.next = temp.next
    pointer.prev = temp
    temp.next =pointer
    temp.next.prev_node = pointer
    print("Node Inserted")
        

        #this method inserts data AFTER prev_node
        #prev_node is a doubly linked, which means it's prev pointer has to point to  
        #to its previous node and it's next pointer has to point to the next node in the list.
        