



class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

#linked list
# 1 -> 2 -> 3 -> 4 -> ->5
class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data, prev_node=None, position=None):

        new_node =Node(data)

        if not self.head:
            self.head = new_node
            return True

        if prev_node:
            temp = prev_node.next
            prev_node.next = new_node
            new_node.next =temp
            return True

            
        
        if position:
            last =self.find_index(index=position)
            if last = self.head
                last.next = self.head
                self.head = last
                return True

            return self.add(data, prev_node=last)
            


    last =self.find_index()
    last.next = new_node
    return True

def find_index(self, index=None):
    last = self.head
    counter = 0
    while (last.next):
        last = last.next
        if counter == index:
            break
        counter += 1
    return last




def removeNode(self, data, target_data  ):
    #delete first item in the list
    # [1] -> [2] -> [3]
    if self.head.data == target_data:
        self.head =self.head.next
        return True
    
    last = self.head
    temp= self.head.next

    while last:
        current = last.next
        if current.data == target_data:
            last.next = current.next
            return True
        last = last.next

    return False
      
    #while prev_node.data is not data:
     #   temp_node = prev_node
      #  prev_node= prev_node.next


        
    
    
    
