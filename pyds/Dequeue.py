"""
Queues

operations:
    enqueue, add elements
    dequeue, removed - returns null if empty

FIRST-IN is FIRST OUT (FIFO)

additional operatinos:
    func to return item at head without removing
    func to return tail of queue without removing
    

dequeue: a double-ended queue
    a doubly linked list which insertions/deletions are from
    one of two ends - head or tail
"""

from pds.DoublyLinkedList import DoublyLinkedList

class Dequeue(DoublyLinkedList):
    
    def __init__(self):
        self.head = None
    
    
    def enqueue(self, item, id):
        node = self.ListNode(item)
        self.setNodeID(node, id)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node
    
    def dequeue(self):
        lastNode = self.poll()
        prevNode = lastNode.prev
        if prevNode:
            prevNode.next = None
        else:
            self.head = None
        return lastNode
    
    def poll(self):
        return self.getLastNode()
        
    def eject(self):
        secondNode = self.head.next
        self.head = secondNode
        secondNode.prev = None

    def max(self):
        return self._max(self.head)
    
    def _max(self, node):
        max_node = node
        while node.next != None:
            if node.data > max_node.data:
                max_node = node
            node = node.next
        return max_node
    
    def iterator(self):
        node = self.head
        while node != None:
            yield node
            node = node.next
    
    def asList(self):
        return [node.data for node in self.iterator()]

def main():
    d = Dequeue()
    d.enqueue(7)
    d.enqueue(6)
    d.enqueue(2)
    d.enqueue(5)
    d.dequeue()
    d.enqueue(10)
    d.eject()
    m = d.max()
    print m.data
    print "should equal 6"