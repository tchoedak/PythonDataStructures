# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:08:07 2016

@author: tenz
"""

class BinaryTree:
    class TreeNode:
        def __init__(self, nid, data):
            self.nid = nid
            self.data = data
            self.parent = None
            self.left = None
            self.right = None
        
        def setLeft(self, node):
            self.left = node
            self.left.parent = self
        
        def setRight(self, node):
            self.right = node
            self.right.parent = self


    def __init__(self):
        
        self.head = None
    
    def getLeftChild(self):
        return self.left
    
    def getRightChild(self):
        return self.right
    
    def setNodeValue(self, data):
        self.data = data
    
    def getNodeValue(self):
        return self.data
    
    def searchID(self, nid):
        return self._searchID(self, nid)
        
    def _searchID(self, node, nid):
        if node.nid == nid:
            return node
        else:
            if node.left:
                k = self._searchID(node.left, nid)
                if k is not None:
                    return k
            if node.right:
                m = self._searchID(node.right, nid)
                if m is not None:
                    return m
    
    def preOrderTraverse(self):
        if self.head:
            self._preOrderTraverse(self.head)
    
    def _preOrderTraverse(self, node):
        print node.nid
        if node.left:
            self._preOrderTraverse(node.left)
        if node.right:
            self._preOrderTraverse(node.right)
    
    def inOrderTraverse(self):
        if self.head:
            self._inOrderTraverse(self.head)
    
    def _inOrderTraverse(self, node):
        if node:
            self._inOrderTraverse(node.left)
            if node:
                print node.nid
            self._inOrderTraverse(node.right)
    
    def postOrderTraverse(self):
        if self.head:
            self._postOrderTraverse(self.head)
    
    def _postOrderTraverse(self, node):
        if node:
            self._postOrderTraverse(node.left)
            self._postOrderTraverse(node.right)
            print node.nid
    
    def height(self, node):
        if not node:
            return -1
        else:
            lefth = self.height(node.left) + 1
            righth = self.height(node.right) + 1
            return max(lefth, righth)

    def createNode(self, nid, data):
        return self.TreeNode(nid, data)
    
    def setRootNode(self, node):
        self.head = node
    
    def setLeftChild(self, parent_node, child_node):
        parent_node.left = child_node
    
    def setRightChild(self, parent_node, child_node):
        parent_node.right = child_node

    def isHeightBalanced(self):
        return self._isHeightBalanced(self.head)
    
    def _isHeightBalanced(self, node):
        if not node:
            return True
        else:
            lh = self.height(node.left)
            rh = self.height(node.right)
        if abs(lh - rh) <= 1 and self._isHeightBalanced(node.left) and self._isHeightBalanced(node.right):
            return True
        else:
            return False
        
        

t = BinaryTree()
t.setRootNode(t.createNode("A", 314))
r = t.head
r.setLeft(t.createNode("B", 6))
r.left.setLeft(t.createNode("C", 271))
r.left.left.setLeft(t.createNode("D", 28))
r.left.left.setRight(t.createNode("E", 0))
r.left.setRight(t.createNode("F", 561))
print a.isHeightBalanced()

a = BinaryTree()
a.setRootNode(a.createNode("A", 1))
b = a.head
b.setLeft(a.createNode("B",6))
b.setRight(a.createNode("C", 8))
b.left.setLeft(a.createNode("D", 3))
b.left.setRight(a.createNode("E", 5))
print b.isHeightBalanced()