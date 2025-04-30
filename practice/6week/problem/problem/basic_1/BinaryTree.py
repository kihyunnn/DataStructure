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
    def getRightCount(self)->int:
        return 0 if self.isEmpty() else self.getRightCount_(self.root)
    def getLeafCount(self)->int:
        return 0 if self.isEmpty() else self.getLeafCount_(self.root)
    def getHeight(self)->int:
        return 0 if self.isEmpty() else self.getHeight_(self.root)
    def getCount_(self, node: BinaryNode)->int:
        if node == None:
            return 0
        ## 1.2) block을 채우시오.
        return 1 + self.getCount_(node.getLeft()) + self.getCount_(node.getRight())
    
    ## 오른쪽 자식 노드를 가지는 노드들의 갯수를 알아내는 함수
    def getRightCount_(self, node: BinaryNode)->int:
        if node == None:
            return 0
        ## 1.3) block을 채우시오.
        if node.getRight() is not None: # 오른쪽 자식 노드가 있으면
            return 1 + self.getRightCount_(node.getLeft()) + self.getRightCount_(node.getRight())
        return self.getRightCount_(node.getLeft()) + self.getRightCount_(node.getRight())
    def getLeafCount_(self, node: BinaryNode)->int:
        if node == None:
            return 0
        ## 1.4) block을 채우시오.
        if node.isLeaf(): # 자식 노드가 없으면
            return 1
        else:
            return self.getLeafCount_(node.getLeft()) + self.getLeafCount_(node.getRight())
    def getHeight_(self, node: BinaryNode)->int:
        if node == None:
            return 0
        ## 1.5) block을 채우시오.
        hLeft = self.getHeight_(node.getLeft())
        hRight = self.getHeight_(node.getRight())
        return hLeft+1 if hLeft > hRight else hRight+1
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
        print("\npreorder: ", end='')
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
    def calcSize(self)->int:
        return self.calcSize_(self.root)
    ## 1.6) block을 채우시오.
    def calcSize_(self, node: BinaryNode)->int:
        if node == None:
            return 0
        return node.getData() + self.calcSize_(node.getLeft()) + self.calcSize_(node.getRight())
    ## 수식 계산 함수
    def evaluate(self)->int:
        return self.evaluate_(self.root)
    def evaluate_(self, node: BinaryNode)->int:
        if node == None:
            return 0
        ## 1.7) block을 채우시오.
        if node.isLeaf(): # 자식 노드가 없으면
            return node.getData()*node.getData()
        else:
            op1 = self.evaluate_(node.getLeft())
            op2 = self.evaluate_(node.getRight())
            
            if node.getData() == '+':
                return op1 + op2
            elif node.getData() == '-':
                return op1 - op2
            elif node.getData() == '*':
                return op1 * op2
            elif node.getData() == '/':
                return op1 / op2
            return 0