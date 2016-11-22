"""
Heaps

aka Priority Queue

where the keys at every node satisfy the heap property:
    key is eq or gt than all keys stored in children

min heap is the opposite

using arrays

parent at position p
left child at position 2p
right child at position 2p+1

node n:
    parent at n/2
    z
    
max heap:
    sum of children is smaller or eq than parent
    
min heap:
    parent is always smaller or eq than either children
"""

class MinHeap:
    
    def __init__(self):
        self.heap = [0]
        self.size = 0
    
    
    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        self.heapifyUp(self.size-1)
    
    def heapifyUp(self, index):
        parent = index/2
        if self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            print "completed a swap! new heap:"
            print self.heap
            self.heapifyUp(parent)
        else:
            return
    
    def delMin(self):
        self.heap[1] = self.heap[self.size - 1]
        self.heap.pop()
        self.size -= 1
        self.heapifyDown(1)
    
    def heapifyDown(self, index):
        child = 2*index
        child2 = 2*index + 1
        #sanity check to make sure childs can be compared to
        if child <= self.size - 1:
            #heap property is violated
            if self.heap[index] > self.heap[child]:
                #if child2 is smaller, swap with it instead
                if self.heap[child2] < self.heap[child]:
                    self.heap[index], self.heap[child2] = self.heap[child2], self.heap[index]
                    print self.heap
                    self.heapifyDown(child2)
                #else heap property hot violated by swapping so go ahead
                else:
                    self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
                    print self.heap
                    self.heapifyDown(child)
            elif self.heap[index] > self.heap[child2]:
                self.heap[index], self.heap[child2] = self.heap[child2], self.heap[index]
                print self.heap
                self.heapifyDown(child2)
            else:
                return

    def buildHeap(self, alist):
        self.heap = [0] + alist[:]
        self.size = len(self.heap)
        index = (self.size - 1)/ 2
        while index > 0:
            self.heapifyDown(index)
            print index
            index -= 1

j = MinHeap()
j.heap = [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
j.size = len(j.heap)
j.delMin()

h = MinHeap()
h.buildHeap([9, 6, 5, 2, 3])
print h.heap
print h.heap == [0, 2, 3, 5, 6, 9]