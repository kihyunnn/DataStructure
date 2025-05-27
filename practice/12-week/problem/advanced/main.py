from typing import Tuple
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
        return node.height if node else 0

    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def rotate_right(self, n):
        x = n.left
        n.left = x.right
        x.right = n
        self.update_height(n)
        self.update_height(x)
        return x

    def rotate_left(self, n):
        x = n.right
        n.right = x.left
        x.left = n
        self.update_height(n)
        self.update_height(x)
        return x

    # --- 심화문제 함수1 ---
    '''
        [1] rebalance() 함수를 완성하라.
    '''
    def rebalance(self, node):
        self.update_height(node)
        balance = self.balance_factor(node)
        if balance > 1: #LR 이거나 LL임
            if self.balance_factor(node.left) < 0: #LR인경우
                node.left = self.rotate_left(node.left) #중간노드 좌회전
            return self.rotate_right(node) #루트노드 우회전
        if balance < -1: # RR이거나 RL임
            if self.balance_factor(node.right) > 0: #RL인경우
                node.right = self.rotate_right(node.right) #중간노드 우회전
            return self.rotate_left(node) #루트노드 좌회전
        return node

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return self.rebalance(node)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _delete(self, node, key):
        if not node:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # successor: 오른쪽 서브트리의 최소값
            succ = node.right
            while succ.left:
                succ = succ.left
            node.key = succ.key
            node.right = self._delete(node.right, succ.key)
        return self.rebalance(node)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def preorder(self, n):
        if not n: return
        print(n.key, end=" ")
        self.preorder(n.left)
        self.preorder(n.right)

    def inorder(self, n):
        if not n: return
        self.inorder(n.left)
        print(n.key, end=" ")
        self.inorder(n.right)

    def postorder(self, n):
        if not n: return
        self.postorder(n.left)
        self.postorder(n.right)
        print(n.key, end=" ")


def count_leaves(node: AVLNode) -> int:
    """자식이 없는 노드(leaf) 개수 반환."""
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


# --- 심화문제 함수2 ---
'''
    [2] merge_avl() 함수를 완성하라. 
'''
def merge_avl(tree1: AVLTree, tree2: AVLTree) -> AVLTree:
    #이건 tree1의 모든 값이 tree2보다 작다는 것을 가정한건가??
    if not tree1.root:
        return tree2
    if not tree2.root:
        return tree1

    node = tree1.root
    while node.right:
        node = node.right #이게 끝나면 node에는 트리1의 가장 큰 노드가 들어가네
    max_key = node.key

    tree1.delete(max_key)

    new_root = AVLNode(max_key)
    new_root.left  = tree1.root
    new_root.right = tree2.root

    new_tree = AVLTree()
    new_tree.root = new_root
    new_tree.root = new_tree.rebalance(new_tree.root)

    return new_tree

# --- 심화문제 함수3 ---
'''
    [3] split_avl() 함수를 완성하라. 
'''
def split_avl(tree: AVLTree, key: int) -> Tuple[AVLTree, AVLTree]:
    def _split(node: AVLNode, key: int):
        if not node:
            return None, None

        if node.key <= key: # 이 노드는 왼쪽 트리에 포함
            left_sub, right_sub = _split(node.right, key)
            node.right = ____
            node = tree.rebalance(node)
            return node, right_sub
        else:
            left_sub, right_sub = _split(____, ____)
            node.left = ____
            node = tree.rebalance(node)
            return left_sub, node

    left_root, right_root = _split(____, ____)
    left_tree, right_tree = AVLTree(), AVLTree()
    left_tree.root, right_tree.root = left_root, right_root
    return left_tree, right_tree

# 출력문 only , 수정X
if __name__ == "__main__":
    aa = AVLTree()
    for x in [10, 20, 30, 40, 50, 29]:
        aa.insert(x)

    print("Preorder:", end=" ")
    aa.preorder(aa.root); print()
    print("Inorder: ", end=" ")
    aa.inorder(aa.root); print()
    print("Postorder:", end=" ")
    aa.postorder(aa.root); print()

    # leaf/internal 노드 개수 출력
    print("Leaf nodes count:", count_leaves(aa.root))

    bb = AVLTree()
    for x in [60, 70, 80]:
        bb.insert(x)
    merged = merge_avl(aa, bb)

    print("Merged Inorder: ", end=" ")
    merged.inorder(merged.root); print()
    print("Merged Preorder:", end=" ")
    merged.preorder(merged.root); print()
    print("Merged postorder:", end=" ")
    merged.postorder(merged.root); print()
    
    # 병합된 트리의 leaf/internal 개수
    print("Merged leaf count:", count_leaves(merged.root))

    spl1, spl2 = split_avl(merged, 40)
    print("spl1 Inorder: ", end=" ")
    spl1.inorder(spl1.root); print()
    print("spl2 Inorder: ", end=" ")
    spl2.inorder(spl2.root); print()
