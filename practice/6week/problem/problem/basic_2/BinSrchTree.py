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
            return self.search_(''' block ''', ''' block ''')
        else:
            return self.search_(''' block ''', ''' block ''')
    
    def insert(self, n: BinaryNode):
        if n == None:
            return
        if self.isEmpty():
            self.root = n
        else:
            self.insert_(self.root, n)
    
    ## 2.3) key를 삽입하는 함수를 구현하시오.
    def insert_(self, r: BinaryNode, n: BinaryNode):
        if n.getData() == ''' block ''':
            return
        elif n.getData() < r.getData():
            if r.getLeft() == None:
                r.setLeft(n)
            else:
                self.insert_(''' block ''', ''' block ''')
        else:
            if r.getRight() == None:
                r.setRight(n)
            else:
                self.insert_(''' block ''', ''' block ''')
    
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
                if ''' block ''' == node:
                    parent.setLeft(None)
                else:
                    parent.setRight(None)
        ## case 2
        elif node.getLeft() == None or node.getRight() == None:
            child = node.getLeft() if node.getLeft() != None else node.getRight()
            if node == self.root:
                self.root = ''' block '''
            else:
                if ''' block ''' == node:
                    parent.setLeft(child)
                else:
                    parent.setRight(child)
        ## case 3
        else:
            succp = node
            succ = ''' block '''
            while succ.getLeft() != None:
                succp = succ
                succ = ''' block '''
            if succp.getLeft() == succ:
                succp.setLeft(''' block ''')
            else:
                succp.setRight(''' block ''')
            node.setData(''' block ''')
            node = succ