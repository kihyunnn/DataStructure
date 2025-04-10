from BinSrchTree import *

'''
    Basic 1. 이진트리 구조 구현하기.
        - 아래에서 보이는 'tree' 트리들에 대해서 각 문제들에서 원하는 데이터 값을 출력하고자 한다.
        - class BinaryTree는 'BinaryTree.py'안에 선언되어 있다.
        - class BinaryNode는 'BinaryNode.py'안에 선언되어 있다.
        - 각 문제에서 원하는 구현이 되도록 모든 block을 채워 넣어라.
'''

def main():
    tree = BinSrchTree()
    
    ## 삽입 연산 테스트
	## 2.1) 아래와 같은 출력이 나올 수 있도록 block을 채우시오.
    tree.insert(BinaryNode(35))
    tree.insert(BinaryNode(''' block '''))
    tree.insert(BinaryNode(7))
    tree.insert(BinaryNode(''' block '''))
    tree.insert(BinaryNode(12))
    tree.insert(BinaryNode(''' block '''))
    tree.insert(BinaryNode(68))
    tree.insert(BinaryNode(''' block '''))
    tree.insert(BinaryNode(''' block '''))
    tree.insert(BinaryNode(99))
    
    tree.inorder()
    tree.preorder()
    tree.postorder()
    tree.levelorder()
    ## -> 출력:
	## inorder: [3] [7] [12] [18] [22] [26] [30] [35] [68] [99]
	## preorder: [35] [18] [7] [3] [12] [26] [22] [30] [68] [99]
	## postorder: [3] [12] [7] [22] [30] [26] [18] [99] [68] [35]
	## levelorder: [35] [18] [68] [7] [26] [99] [3] [12] [22] [30]
    
    print(f"노드의 개수 = {tree.getCount()}")
    print(f"단말의 개수 = {tree.getLeafCount()}")
    print(f"트리의 높이 = {tree.getHeight()}")
    
    ## 삭제 연산 테스트
    print("삭제: case 1 ==> 노드 3 삭제")
    tree.remove(3)
    tree.levelorder()
    print("삭제: case 2 ==> 노드 68 삭제")
    tree.remove(68)
    tree.levelorder()
    print("삭제: case 3 ==> 노드 18 삭제")
    tree.remove(18)
    tree.levelorder()
    print("삭제: case 3 ==> 노드 35 삭제 (루트 노드 삭제)")
    tree.remove(35)
    tree.levelorder()
    
    ## 최종 트리 정보 출력
    print(f"노드의 개수 = {tree.getCount()}")
    print(f"단말의 개수 = {tree.getLeafCount()}")
    print(f"트리의 높이 = {tree.getHeight()}")

if __name__ == "__main__":
    main()