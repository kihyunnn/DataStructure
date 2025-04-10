from BinaryTree import *

'''
    Basic 1. 트리 구조 구현하기.
        - 아래에서 보이는 'tree', 'tree2', 'tree3' 트리들에 대해서 각 문제들에서 원하는 데이터 값을 출력하고자 한다.
        - class BinaryTree는 'BinaryTree.py'안에 선언되어 있다.
        - class BinaryNode는 'BinaryNode.py'안에 선언되어 있다.
        - 각 문제에서 원하는 구현이 되도록 모든 block을 채워 넣어라.
'''

def main():
    tree = BinaryTree()
    ##          |------- A ------|
    ##      |-- B --|        |-- C
    ##      D       E        F
    d = BinaryNode('D', None, None)
    e = BinaryNode('E', None, None)
    b = BinaryNode('B', d, e)
    f = BinaryNode('F', None, None)
    c = BinaryNode('C', f, None)
    a = BinaryNode('A', b, c)
    tree.setRoot(a)
    
    print(f"노드의 개수 = {tree.getCount()}")
    print(f"오른쪽 자식 노드를 가지는 노드의 개수 = {tree.getRightCount()}")
    print(f"단말의 개수 = {tree.getLeafCount()}")
    print(f"트리의 높이 = {tree.getHeight()}")
    
    ## 전위, 중위, 후위에 대한 함수들은 따로 문제화 시키지 않았습니다. 그러나, 시간이 날 때 공부해보시길 바랍니다.
    tree.inorder()
    tree.preorder()
    tree.postorder()
    tree.levelorder()
    
    tree2 = BinaryTree()
	##          |------ + ------|
	##      |-- * --|       |-- - --|
	##      3       2       5       6
    n1 = BinaryNode(3, None, None)
    n2 = BinaryNode(2, None, None)
    n3 = BinaryNode('*', n1, n2)
    n4 = BinaryNode(5, None, None)
    n5 = BinaryNode(6, None, None)
    n6 = BinaryNode('-', n4, n5)
    n7 = BinaryNode('+', n3, n6)
    tree2.setRoot(n7)
    
    ## -> ((3^2) * (2^2)) + ((5^2) - (6^2))
	## -> 각 수를 제곱해서 주어진 기호대로 사칙연산 했을 때의 계산 결과 = 25
    print(f"각 수를 제곱해서 주어진 기호대로 사칙연산 했을 때의 계산 결과 = {tree2.evaluate()}")
    
    tree3 = BinaryTree()
	##          |------ 0 ---------|
	##          50            |-- 100 --|
	##                       200       500
    m4 = BinaryNode(200, None, None)
    m5 = BinaryNode(500, None, None)
    m3 = BinaryNode(100, m4, m5)
    m2 = BinaryNode(50, None, None)
    m1 = BinaryNode(0, m2, m3)
    tree3.setRoot(m1)

	## -> 디렉토리 용량 계산 결과 = 850 KB
    print(f"디렉토리 용량 계산 결과 = {tree3.calcSize()} KB")
 

if __name__ == "__main__":
    main()