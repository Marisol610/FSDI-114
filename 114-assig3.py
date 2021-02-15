class Queue:
def __init__(self):
    self.items = []

def is_empty(self):
    return self.items == []

def enqueue(self, item):
    self.items.insert(0, item)

def dequeue(self):
    return self.items.pop()

def size(self):
    return len(self.items)



def reverse(string):
    my_stack = Stack()

    for char in string:
        my_stack.push(char)
    out =""
    while not my_stack.is_empty():
        out +=my_stack.pop()
    return out


if __name__== "__main__":
    print(reverse("hello"))







class Queue2Stacks:
def __init__(self):

self.stack1 = []
self.stack2 = []

def enqueue(self, element):
self.stack1.append(element)
pass

def dequeue(self):
    if not self.stack2:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()