from BinaryTree import *

class BinSrchTree(BinaryTree):
    def __init__(self):
        super().__init__() 
    def search(self, key: int)->BinaryNode:
        node = self.search_(self.root, key)
        if node != None:
            print(f"탐색 성공: 키값이 {node.getData()}인 노드 있음")
        else:
            print(f"탐색 실패: 키값이 {key}인 노드 없음")
        return node
    ## 2.2) key를 검색하는 함수를 구현하시오.
    def search_(self, n: BinaryNode, key: int)->BinaryNode:
        if n == None:
            return None
        if key == n.getData():
            return n
        elif key < n.getData():
            return self.search_(n.getLeft(), key)  
        else:
            return self.search_(n.getRight(), key)  
    
    def insert(self, n: BinaryNode):
        if n == None:
            return
        if self.isEmpty():
            self.root = n
        else:
            self.insert_(self.root, n)
    
    ## 2.3) key를 삽입하는 함수를 구현하시오.
    def insert_(self, r: BinaryNode, n: BinaryNode):
        if n.getData() == r.getData():  
            return
        elif n.getData() < r.getData():
            if r.getLeft() == None:
                r.setLeft(n)
            else:
                self.insert_(r.getLeft(), n)
        else:
            if r.getRight() == None:
                r.setRight(n)
            else:
                self.insert_(r.getRight(), n)
    
    def remove(self, data: int):
        if self.isEmpty():
            return
        parent = None
        node = self.root
        while node != None and node.getData() != data:
            parent = node
            node = node.getLeft() if data < node.getData() else node.getRight()
        if node == None:
            print("Error: key is not in the tree!")
            return
        else:
            self.remove_(parent, node)
    ## 2.4) key를 삭제하는하는 함수를 구현하시오.
    def remove_(self, parent: BinaryNode, node: BinaryNode):
        ## case 1
        if node.isLeaf():
            if parent == None:
                self.root = None
            else:
                if parent.getLeft() == node:
                    parent.setLeft(None)
                else:
                    parent.setRight(None)
        ## case 2
        elif node.getLeft() == None or node.getRight() == None:
            child = node.getLeft() if node.getLeft() != None else node.getRight()
            if node == self.root:
                self.root = child
            else:
                if parent.getLeft() == node:
                    parent.setLeft(child)
                else:
                    parent.setRight(child)
        ## case 3
        else:
            succp = node
            succ = node.getRight()
            while succ.getLeft() != None:
                succp = succ
                succ = succ.getLeft()
            if succp.getLeft() == succ:
                succp.setLeft(succ.getRight())
            else:
                succp.setRight(succ.getRight())
            node.setData(succ.getData())
            node = succ