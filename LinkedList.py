# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 11:28:04 2016

@author: tenz
"""

class LinkedList:
    
    class ListNode:
        
        def __init__(self, data):
            self.data = data
            self.next = None


    def __init__(self):
        self.head = None
    
    def search(self, key):
        if self.head == None:
            return None
        else:
            return self._search(key, self.head)
    
    def _search(self, key, node):
        if node.data == key:
            return node
        elif node.next == None:
            #at the end of linkedList, so node doesnt exist
            return None
        else:
            return self._search(key, node.next)

    def getLastNode(self):
        if self.head == None:
            return None
        else:
            return self._getLastNode(self.head)
    
    def _getLastNode(self, node):
        if node.next == None:
            return node
        else:
            return self._getLastNode(node.next)
    
    def addToEnd(self, data):
        newnode = self.ListNode(data)
        if self.head == None:
            self.head = newnode
        else:
            lastNode = self.getLastNode()
            self._addAfter(lastNode, newnode)
            
    def _addAfter(self, node, newnode):
        newnode.next = node.next
        node.next = newnode
        
    def addAfter(self, key, data):
        newnode = self.ListNode(data)
        node = self.search(key)
        self._addAfter(node, newnode)
    
    def deleteNextNode(self, key):
        node = self.search(key)
        self._deleteNextNode(node)
    
    def _deleteNextNode(self, node):
        node.next = node.next.next

    def iterator(self):
        return self._iterator(self.head)
    
    def _iterator(self, node):
        while node is not None:
            yield node
            node = node.next
            
    def asList(self):
        return [node.data for node in self.iterator()]
    
    def isCycle(self):
        if self.getCycleStart() != None:
            return True
    
    def getCycleStart(self):
        slow = self.head
        fast = self.head
        while (fast != None and fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
        
    def cycleLength(self):
        start = self.getCycleStart()
        end = start.next
        cycleLen = 1
        while start != end:
            cycleLen += 1
            end = end.next
        return cycleLen
        
        
                

j = LinkedList()
j.addToEnd(1)
j.addToEnd(2)
j.addToEnd(4)
j.addAfter(2,3)

cycleNode = ListNode(5)
firstNode = j.search(1)
cycleNode.next = firstNode
j.getLastNode().next = cycleNode

