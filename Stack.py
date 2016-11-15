"""
Stacks

operations:
    push
    pop
    peek
    can be implemented using arrays, linkedlists or dynamically sized arrays

    these operations are O(1)
    LAST-IN- is the FIRST-OUT (LIFO)

use cases:
    good for reverse iterators
    when its difficult to step back from a given element
    printing a linkedlist in reverse
    good for parsing in general (regexp)

common problems:
    often want a MAX function
    kept by having M = max(M,e) whenever pushing element e
    but when popping M becomes unreliable if 
    e in pop() happened to be the max
    solved by caching at entry e. ex:
        push(e) -> cache(e, previous_M)
    so when pop(e), M = cache(e, M)
"""

class Stack:
    """array based stack with cacheing"""
    
    def __init__(self):
        self.stack = []
        self.size = 0
        self.cache = {}
        self.max = 0
    
    def push(self, e):
        self.stack.append(e)
        self.size += 1
        #skip caching if e is smaller than previous max
        if e > self.max:
            self.max = e
            self.cache[(e, self.size)] = self.max

    def pop(self):
        self.stack.pop(self.size - 1)
        self.size -= 1
        
        e = self.peek()
        s = self.size
        self.max = self.cache[(e, s)]
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[self.size - 1]

    def isEmpty(self):
        return self.size == 0

    def max(self):
        return self.max

        
j = Stack()
j.push(1)
j.push(2)
j.push(3)
print j.max
j.push(4)
print j.max
j.push(4)
print j.max
j.pop()
print j.max
j.pop()
print j.max