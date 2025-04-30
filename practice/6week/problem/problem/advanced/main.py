from BinaryTree import *

'''
    Adavanced. 주어진 트리에 대한 다양한 함수 구현.
        - 아래에서 보이는 'tree', 'tree2'를 각 문제들에서 원하는 데이터 트리 구조로 만들고자 한다.
        - class BinaryTree는 'BinaryTree.h'안에 선언되어 있다.
        - class TNode는 'BinaryNode.h'안에 선언되어 있다.
        - 각 문제에서 원하는 구현이 되도록 모든 block을 채워 넣어라.
'''

def main():
    tree = BinaryTree()
    
    ##           A
	##       B       E
	##     C   D        F 
    c = BinaryNode('C', None, None)
    d = BinaryNode('D', None, None)
    f = BinaryNode('F', None, None)
    b = BinaryNode('B', c, d)
    e = BinaryNode('E', None, f )
    a = BinaryNode('A', b, e)
    tree.setRoot(a)
    
    ## tree.getCount(), tree.getLeafCount(), tree.getHeight()는 basc2에 있는 함수들과 동일합니다.
    print(f"노드 개수 = {tree.getCount()}")
    print(f"단말 개수 = {tree.getLeafCount()}")
    print(f"트리 높이 = {tree.getHeight()}")
    
    tree.preorder() # preorder:  [A]  [B]  [C]  [D]  [E]  [F] 
    '''
        [3.1] 이진트리가 완전 이진트리인지를 검사하는 다음 연산을 구현하라.
        위에서 주어진 트리는 완전 이진트리가 아니므로 'false'가 반환되어야 한다.
	'''
    print("\n(1)")
    tree.isFull()
    
    '''
        [3.2] 임의의 node의 레벨에 구하는 연산을 구현하라.
	    만약 Node가 트리 안에 있지 않으면 0을 반환하라. 위 이진트리에 대한 레벨은 아래 출력을 참고하라.
    '''
    print("(2)")
    tree.calcLevel(a)
    tree.calcLevel(b)
    tree.calcLevel(c)
    tree.calcLevel(d)
    tree.calcLevel(e)
    tree.calcLevel(f)
    print()
    '''
        -> 출력:
        노드의 레벨은 1.
        노드의 레벨은 2.
        노드의 레벨은 3.
        노드의 레벨은 3.
        노드의 레벨은 2.
        노드의 레벨은 3.
    '''
    '''
        [3.3] 이진트리의 모든 노드에서 왼쪽 서브트리와 오른쪽 서브트리의 높이의 차이가 2보다 
        작으면 이 트리를 "균형이 잡혀 있다(balanced)"라고 한다. 현재 이진트리가 균형 잡혀 있는지를
        검사하는 다음 연산을 구현하라.

        위의 트리는 높이의 차이가 1 이하로 균형 잡혀 있다.
    '''
    print("(3)")
    tree.isBalanced()
    '''
        -> 출력:
        균형잡힌 이진트리입니다.
	'''

    '''
        [3.4] 이진트리의 경로의 길이(path length)를 루트에서부터 모든 자식 노드까지의 경로의 길이의
        합이라고 하자. 경로의 길이를 구하는 다음 연산을 구현하라.

        위의 트리에서 경로의 길이는 0+1+1+2+2+2=8이다.
    '''
    print("(4)")
    tree.pathLength()
    '''
        -> 출력:
        전체 경로의 길이는 8입니다.
    '''
    
    ## [3.5] 이진트리를 좌우로 대칭시키는 다음 연산을 구현하라. 위의 그래프에 대한 대칭 연산 결과는 아래와 같다.
    print("(5)")
    tree.reverse()
    tree.preorder()
    '''
        -> 출력:
        트리의 좌우를 교환합니다.
        preorder:  [A]  [E]  [F]  [B]  [D]  [C] 
    '''
    
    '''
        [3.6] 현재 트리와 that 트리가 같은 노드를 가지지 않으면 두 트리는 분리되어(disjoint) 있다.
        이것을 판단하는 연산을 순환을 이용하여 구현하라.
    '''
    print("(6)")
    tmp = "합니다" if tree.isDisjointFrom(b, e) else "하지 않습니다"
    print(f"루트b인 트리와 루트e인 트리는 Disjoint{tmp}.\n")
    '''
        -> 출력:
        루트b인 트리와 루트e인 트리는 Disjoint 합니다.
    '''
    
    '''
        [3.7] 모든 서브트리가 서로 분리되어 있으면 이 트리는 "유효하다(vaild)"라고 판단한다.
        트리가 유효한지를 판단하는 다음 연산을 구현하라.
    '''
    print("(7)")
    tree.isValid()
    '''
        -> 출력:
        Valid한 이진트리입니다.
    '''
 

if __name__ == "__main__":
    
    main()