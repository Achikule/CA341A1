class TreeNode:
    """Creating a node object that accepts dictionaries"""
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)


class BinarySearchTree:
    """BST with insertion and search. Special attributes for setting and getting indexes. Contains for debugging"""
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key, val):
        if self.root:
            self._insert(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _insert(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._insert(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._insert(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.insert(k, v)

    def search(self, key):
        if self.root:
            res = self._search(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _search(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._search(key, currentNode.leftChild)
        else:
            return self._search(key, currentNode.rightChild)

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        if self._search(key, self.root):
            return True
        else:
            return False

