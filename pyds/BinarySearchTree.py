class BinarySearchTree:
    
    class TreeNode:
        def __init__(self, val):
            self.left = None
            self.right = None
            self.data = val

            
    def __init__(self):
        self.root = None
    
    def getRoot(self):
        return self.root
            
    def add(self, val):
        if (self.root == None):
            self.root = self.TreeNode(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if (val < node.data):
            if (node.left != None):
                self._add(val, node.left)
            else:
                node.left = self.TreeNode(val)
        else:
            if (node.right != None):
                self._add(val, node.right)
            else:
                node.right = self.TreeNode(val)
    
    def find(self, val):
        if (self.root != None):
            return self._find(val, self.root)
        else:
            return None
    
    def _find(self, val, node):
        if (val == node.data):
            return node
        elif (val < node.data and node.left != None):
            self._find(val, node.left)
        elif (val > node.data and node.right != None):
            self._find(val, node.right)
    
    def printInOrder(self, node):
        if (node != None):
            self.printInOrder(node.left)
            print(node.data)
            self.printInOrder(node.right)
    
    def deleteTree(self):
        self.root = None
    
    def printTree(self):
        if (self.root != None):
            self._printTree(self.root)
    
    def _printTree(self, node):
        if (node != None):
            self._printTree(node.left)
            print str(node.data) + ' '
            self._printTree(node.right)

def main():
    #here's where the test runs
    test = binarySearchTree()
    test.add(200)
    test.add(100)
    test.add(300)
    
    f = test.find(test.root, 100)
    
    test.find(test.root, 200)
    test.find(test.root, 100)
    
    def checkIsTree(Tree):
        root = Tree.getRoot()
        return checkNode(root)
        
    # case 1:
    # node1: 100
    # node1.left: 50
    # node2.right: 150

#

def checkNode(node):
    if node.left is not None:
        if node.left.data > node.data:
            return False
    if node.right is not None:
        if node.right.data < node.data:
            return False
    if (node.left is not None and node.right is not None):
        if (not checkNode(node.left) and not checkNode(node.right)):
            return False
    return True


def isBST(node):
    INT_MAX = 4294967296
    INT_MIN = -4294967296
    return (isBSTUtil(node, INT_MIN, INT_MAX))

def isBSTUtil(node, mini, maxi):
     
    # An empty tree is BST
    if node is None:
        return True
 
    # False if thsi node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False
 
    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data -1) and
          isBSTUtil(node.right, node.data+1, max))