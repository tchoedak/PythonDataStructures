# -*- coding: utf-8 -*-

import tchoedak.pythondatastructures.LinkedList

class DoublyLinkedList(LinkedList):
    
    class ListNode:
        
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None


    def __init__(self):
        self.head = None

    def _addAfter(self, node, newnode):
        newnode.next = node.next
        node.next = newnode
        newnode.prev = node

    def _deleteNextNode(self, node):
        node.next = node.next.next
        node.next.prev = node
    
    def _deleteBeforeNode(self, node):
        node.prev = node.prev.prev
        node.prev.next = node
    
    def deleteBeforeNode(self, key):
        node = self.search(key)
        self._deleteBeforeNode(node)