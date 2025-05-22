class AVLNode:
    def __init__(self, key, height=1, left=None, right=None):
        self.key = key
        self.height = height
        self.left = left
        self.right = right

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node):
        if not node:
            return 0
        else:
            b_f = self.height(node.left) - self.height(node.right)
        '''
            [1.1] balance_factor() 함수를 완성하라.
        '''
        return b_f
    '''
        [1.2] rotate_right() 함수와 rotate_left() 함수를 완성하라.
    '''
    def rotate_right(self, n): #오른쪽 회전
        x = n.left
        n.left = x.right
        ## block ##
        x.right = n
        ###########
        ## block ##
        ###########
        self.update_height(n)
        self.update_height(x)
        return x

    def rotate_left(self, n): #왼쪽 회전
        x = n.right
        n.right = x.left
        ## block ##
        x.left = n
        ###########
        ## block ##
        ###########
        self.update_height(n)
        self.update_height(x)
        return x
    '''
        [1.3] rebalance() 함수를 완성하라.
    '''
    def rebalance(self, node):
        self.update_height(node)
        balance = self.balance_factor(node)
        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left =self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node
    
    '''
        [1.4] _insert() 함수를 완성하라.
    '''
    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return self.rebalance(node)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    '''
        [1.5] _delete() 함수를 완성하라.
    '''
    def _delete(self, node, key):
        if not node:
            return node
        elif key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self.min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return self.rebalance(node)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def preorder(self, n):
        print(str(n.key), end=" ")
        if n.left:
            self.preorder(n.left)
        if n.right:
            self.preorder(n.right)
            
    def inorder(self, n):
        if n.left:
            self.inorder(n.left)
        print(str(n.key), end=" ")
        if n.right:
            self.inorder(n.right)
            
    def postorder(self, n):
        if n.left:
            self.postorder(n.left)
        if n.right:
            self.postorder(n.right)
        print(str(n.key), end=" ")
