from __future__ import annotations

class BinaryNode:
    def __init__(self, val, l: BinaryNode=None, r: BinaryNode=None):
        self.data = val
        self.left = l
        self.right = r
    def setData(self, val):
        self.data = val
    def setLeft(self, l: BinaryNode):
        self.left = l
    def setRight(self, r: BinaryNode):
        self.right = r
    def getData(self):
        return self.data
    def getLeft(self)->BinaryNode:
        return self.left
    def getRight(self)->BinaryNode:
        return self.right
    ## 1.1) isLeaf는 자식 노드가 없을 때 1을 반환하는 함수이다. block을 채워라.
    def isLeaf(self):
        return self.left is None and self.right is None