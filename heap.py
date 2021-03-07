class HeapNode():
    def __init__(self, value, parent=None, priority=0, cost=0):
        self.value = value
        self.priority = priority
        self.parent = parent
        self.cost = cost

class Heap():

    def __init__(self):
        # Initialized to help with index math.
        self.heap_list = [None]
        self.count = 0
    
    def __parent_idx(self, idx):
        return idx // 2
    
    def __left_child_idx(self, idx):
        return idx * 2
    
    def __right_child_idx(self, idx):
        return (idx * 2) + 1
    
    def empty(self):
        return self.count == 0
    
    def size(self):
        return self.count
    
    def peek(self):
        if self.heap_list:
            return self.heap_list[1].value
        else:
            return None
    
    def add(self, *nodes):
        for node in nodes:
            self.heap_list.append(node)
            self.count += 1
            self.__rebalance_up(self.count)
    
    def __rebalance_up(self, idx):
        parent_idx = self.__parent_idx(idx)
        new_node = self.heap_list[idx]
        parent_node = self.heap_list[parent_idx]

        if not parent_node:
            return
            
        if new_node.priority < parent_node.priority:
            self.heap_list[idx] = parent_node
            self.heap_list[parent_idx] = new_node
            self.__rebalance_up(parent_idx)
        else:
            return
        
    def retrieve(self):
        if not self.empty():
            root = self.heap_list[1]
            deepest_leaf = self.heap_list.pop(self.count)
            self.count -= 1
            if not self.empty():
                self.heap_list[1] = deepest_leaf
                self.__rebalance_down(1)
            return root
        return None
    
    def __rebalance_down(self, idx):
        left_child_idx = self.__left_child_idx(idx)
        right_child_idx = self.__right_child_idx(idx)
        new_node = self.heap_list[idx]

        if left_child_idx > self.count or right_child_idx > self.count:
            return

        left_child = self.heap_list[left_child_idx]
        right_child = self.heap_list[right_child_idx]

        priorities = [left_child.priority, right_child.priority, new_node.priority]

        if min(priorities) == left_child.priority:
            self.heap_list[left_child_idx] = new_node
            self.heap_list[idx] = left_child
            self.__rebalance_down(left_child_idx)
        elif min(priorities) == right_child.priority:
            self.heap_list[right_child_idx] = new_node
            self.heap_list[idx] = right_child
            self.__rebalance_down(right_child_idx)
        else:
            return

    def print(self):
        if self.empty():
            print('Empty heap')
            return

        for node in self.heap_list[1:]:
            print('Value: ', node.value, ' Priority: ', node.priority)
        print()

'''
tasks = {
    'homework': 2,
    'baking': 1,
    'clean tables': 5,
    'pet dog': 5,
    'wear clothes': 4,
    'shower': 6,
    'brush teeth': 3,
    'eat': 10,
    'poop': 4
}

heap = Heap()
for task, priority in tasks.items():
    node = HeapNode(task, priority)
    heap.add(node)
heap.print()
heap.retrieve()
heap.print()
heap.retrieve()
heap.print()
heap.retrieve()
heap.print()
heap.retrieve()
heap.print()
heap.retrieve()
heap.print()
heap.retrieve()
heap.print()
heap.retrieve()
heap.print()
heap.retrieve()
heap.print()
heap.retrieve()
heap.print()
heap.retrieve()
heap.print()
heap.retrieve()
heap.print()
'''



