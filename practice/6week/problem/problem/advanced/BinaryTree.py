from BinaryNode import *

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
    def preorder(self):
        print("preorder: ", end='')
        self.preorder_(self.root)
        print("\n")
    def preorder_(self, node: BinaryNode):
        if node != None:
            print(f"[{node.getData()}] ", end='')
            if node.getLeft() != None:
                self.preorder_(node.getLeft())
            if node.getRight()!= None:
                self.preorder_(node.getRight())
    ## 3.1) block을 채우시오.
    def isEven(self, n: BinaryNode)->bool:
        if n == None or (''' block ''' == None and ''' block ''' == None):
            return True
        if n.getLeft() == None or n.getRight() == None:
            return False
        
        return self.isEven(n.getLeft()) and self.isEven(n.getRight())
    def isFull(self)->bool:
        ret = self.isEven(self.root)
        tmp = "입니다" if ret else "가 아닙니다"
        print(f"완전이진트리{tmp}\n")
        return ret
    def checkLevel(self, p: BinaryNode, n: BinaryNode, level: int)->int:
        ## 3.2) block을 채우시오.
        ll, lr = 0, 0
        if ''' block ''': # 현재 노드가 찾고자 하는 Node와 같다면
            return level
        
        ## 3.3) block을 채우시오.
        if p.getLeft() != None:
            ll = self.checkLevel(p.getLeft(), n, ''' block ''')
        if p.getRight() != None:
            lr = self.checkLevel(p.getRight(), n, ''' block ''')
            
        if ll > 0:
            return ll
        else:
            return lr
    ## 3.4) block을 채우시오
    def calcLevel(self, n: BinaryNode)->int:
        level = 0
        if self.root != None:
            level = self.checkLevel(self.root, n, ''' block ''')
        
        if level > 0:
            print(f"노드의 레벨은 {level}.")
        else:
            print("트리에 없는 노드입니다.")
        return level
    def checkBalanced(self, p: BinaryNode):
        if p == None:
            return True
        lh = self.getHeight_(p.getLeft())
        rh = self.getHeight_(p.getRight())
        dh = rh - lh
        
        ## 3.5) block을 채우시오.
        if ''' block ''' or ''' block ''': # unbalanced가 되려면 dh의 조건은?
            return False
        
        if self.checkBalanced(p.getLeft()) == 0:
            return False
        
        return self.checkBalanced(p.getRight())
    
    def isBalanced(self)->bool:
        ret = self.checkBalanced(self.root)
        tmp = "균형잡힌" if ret else "불균형적인"
        print(f"{tmp} 이진트리입니다.\n")
        return ret
    def calcPathLength(self, p: BinaryNode, level: int)->int:
        llen, rlen = 0, 0
        if p == None:
            return 0
        
        ## 3.6) block을 채우시오.
        llen = self.calcPathLength(p.getLeft(), level+1)
        rlen = self.calcPathLength(p.getRight(), level+1)
        
        return ''' block ''' + ''' block ''' + ''' block '''
    
    def pathLength(self)->int:
        len = self.calcPathLength(self.root, 0)
        print(f"전체 경로의 길이는 {len}입니다.\n")
        return len
    
    def swapNodes(self, p: BinaryNode):
        if p == None:
            return
        
        ## 3.7) block을 채우시오.
        if p.getLeft() == None and p.getRight() != None:
            p.left, p.right = ''' block ''', None
        ## 3.8) block을 채우시오.
        elif p.getLeft() != None and p.getRight() == None:
            p.left, p.right = None, ''' block '''
        ## 3.9) block을 채우시오.
        elif p.getLeft() != None and p.getRight() != None:
            p.left, p.right = ''' block ''', ''' block '''
        
        self.swapNodes(p.getLeft())
        self.swapNodes(p.getRight())
    
    def reverse(self):
        print("트리의 좌우를 교환합니다.")
        self.swapNodes(self.root)
    
    def hasSameNode(self, p: BinaryNode, n: BinaryNode)->int:
        if n == None or p == None:
            return 0
        if n == p:
            return 1
        ## 3.10) block을 채우시오.
        return self.hasSameNode(''' block ''', n) + self.hasSameNode(''' block ''', n)
    
    def isDisjointFrom(self, p: BinaryNode, n: BinaryNode)->int:
        if p == None or n == None:
            return 1
        if self.hasSameNode(p, n):
            return 0
        if self.hasSameNode(p, n.getLeft()):
            return 0
        if self.hasSameNode(p, n.getRight()):
            return 0
        return 1

    def checkValid(self, n: BinaryNode)->int:
        if n == None:
            return 1
        
        ## 3.11) block을 채우시오.
        if self.isDisjointFrom(''' block ''', ''' block ''') == 0:
            return 0

        if self.checkValid(n.getLeft()) == 0:
            return 0

        if self.checkValid(n.getRight()) == 0:
            return 0

        return 1
    
    def isValid(self)->int:
        ret = self.checkValid(self.root)
        tmp = "Valid한" if ret else "Valid하지 않은"
        print(f"{tmp} 이진트리입니다.\n")
        return ret