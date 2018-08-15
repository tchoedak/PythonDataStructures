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

class MaxHeap:
    
    def __init__(self):
        self.heap = ['head']
        self.size = 0
    
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def insert(self, data):
        self.heap.append(data)
        self.size += 1
        print "heapifying index:"
        self.heapifyUp(self.size)

    def heapifyUp(self, index):
        parent = index/2
        if self.heap[parent] == 'head':
            return
        elif self.heap[index] > self.heap[parent]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self.heapifyUp(parent)
        else:
            return

    def delMax(self):
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.heapifyDown(1)

    def heapifyDown(self, index):
        child = 2*index
        child2 = 2*index + 1
        #sanity check to make sure childs can be compared to
        if child <= self.size:
            if child2 <= self.size:
                if self.heap[child] > self.heap[child2]:
                    max_child = child
                else:
                    max_child = child2
                
                if self.heap[index] < self.heap[max_child]:
                    self.heap[index], self.heap[max_child] = self.heap[max_child], self.heap[index]
                    self.heapifyDown(max_child)
            else:
                if self.heap[index] < self.heap[child]:
                    self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
                    self.heapifyDown(child)


    def buildHeap(self, alist):
        self.heap = [0] + alist[:]
        self.size = len(self.heap) - 1
        index = self.size/ 2
        while index > 0:
            self.heapifyDown(index)
            print index
            index -= 1

def main():
    k = MaxHeap()
    k.insert(10)
    k.insert(7)
    k.insert(4)
    k.insert(8)
    k.heap
    
    k.delMax()
    k.heap
    
    j = MaxHeap()
    j.insert(15)
    j.insert(4)
    j.insert(9)
    j.insert(11)
    j.insert(3)
    j.insert(5)
    j.insert(7)
    j.insert(14)
    j.heap
    j.delMax()
    j.heap


