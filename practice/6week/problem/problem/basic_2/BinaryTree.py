from BinaryNode import *
from CircularQueue import *

class BinaryTree:
    def __init__(self):
        self.root = None
    def setRoot(self, node: BinaryNode):
        self.root = node
    def getRoot(self)->BinaryNode:
        return self.root
    def isEmpty(self)->bool:
        return self.root == None
    def getCount(self)->int:
        return 0 if self.isEmpty() else self.getCount_(self.root)
    def getLeafCount(self)->int:
        return 0 if self.isEmpty() else self.getLeafCount_(self.root)
    def getHeight(self)->int:
        return 0 if self.isEmpty() else self.getHeight_(self.root)
    def getCount_(self, node: BinaryNode)->int:
        if node == None:
            return 0
        ## 1.2) block을 채우시오.
        return 1 + ''' block ''' + ''' block '''
    def getLeafCount_(self, node: BinaryNode)->int:
        if node == None:
            return 0
        ## 1.4) block을 채우시오.
        if ''' block ''': # 자식 노드가 없으면
            return 1
        else:
            return ''' block ''' + ''' block '''
    def getHeight_(self, node: BinaryNode)->int:
        if node == None:
            return 0
        ## 1.5) block을 채우시오.
        hLeft = ''' block '''
        hRight = ''' block '''
        return hLeft+1 if ''' block ''' else ''' block '''
    def inorder(self):
        print("\ninorder: ", end='')
        self.inorder_(self.root)
    def preorder(self):
        print("\npreorder: ", end='')
        self.preorder_(self.root)
    def postorder(self):
        print("\npostorder: ", end='')
        self.postorder_(self.root)
    def inorder_(self, node: BinaryNode):
        if node != None:
            if node.getLeft() != None:
                self.inorder_(node.getLeft())
            print(f"[{node.getData()}]", end='')
            if node.getRight()!= None:
                self.inorder_(node.getRight())
    def preorder_(self, node: BinaryNode):
        if node != None:
            print(f"[{node.getData()}]", end='')
            if node.getLeft() != None:
                self.preorder_(node.getLeft())
            if node.getRight()!= None:
                self.preorder_(node.getRight())
    def postorder_(self, node: BinaryNode):
        if node != None:
            if node.getLeft() != None:
                self.postorder_(node.getLeft())
            if node.getRight()!= None:
                self.postorder_(node.getRight())
            print(f"[{node.getData()}]", end='')
    def levelorder(self):
        print("\nlevelorder: ", end='')
        if not self.isEmpty():
            q = CircularQueue()
            q.enqueue(self.root)
            while(not q.isEmpty()):
                n = q.dequeue()
                if n != None:
                    print(f"[{n.getData()}]", end='')
                    q.enqueue(n.getLeft())
                    q.enqueue(n.getRight())
        print()