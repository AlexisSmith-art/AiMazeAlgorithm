from node import Node

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def empty(self):
        return self.length == 0
    
    def size(self):
        return self.length
    
    def peek(self):
        if self.head:
            return self.head.value
        else:
            return None

    def add(self, *nodes):
        for node in nodes:
            node.next = self.head
            self.head = node
            self.length += 1
    
    def retrieve(self):
        if not self.empty():
            node = self.head
            if node.next:
                self.head = node.next
            else:
                self.head = None
            self.length -= 1
            return node
        return None

'''
stack = Stack()
stack.add('apple')
stack.add('orange')
stack.add('banana')
print(stack.peek())
print(stack.retrieve())
print(stack.retrieve())
print(stack.retrieve())
print(stack.retrieve())
print(stack.retrieve())
'''