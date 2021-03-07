from node import Node

class Queue:
    def __init__(self):
        self.head = self.tail = None
        self.count = 0
    
    def empty(self):
        return self.count == 0

    def size(self):
        return self.count

    def peek(self):
        if self.head:
            return self.head.value
        else:
            return None

    def add(self, *nodes):
        for node in nodes:
            if not self.head:
                self.head = self.tail = node
            else:
                self.tail.next = node
                self.tail = node
            self.count += 1

    def retrieve(self):
        if not self.empty():
            node = self.head
            self.head = self.head.next
            self.count -= 1
            return node
        return None
'''
queue = Queue()
queue.add('apples', 'bananas', 'oranges')
print(queue.peek())
print(queue.peek())
print(queue.size())
print(queue.retrieve())
print(queue.retrieve())
print(queue.retrieve())
print(queue.retrieve())
print(queue.size())
'''