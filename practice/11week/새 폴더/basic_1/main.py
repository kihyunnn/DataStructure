from AVLTree import AVLTree

'''
    Basic_1. AVLTree 클래스의 다양한 함수 구현.
        - [1.1] balance_factor()
        - [1.2] rotate_right(), rotate_left()
        - [1.3] rebalance()
        - [1.4] insert()
        - [1.5] delete()
'''

if __name__=="__main__":
    aa = AVLTree()
    aa.insert(10)
    aa.insert(20)
    aa.insert(30)
    aa.insert(40)
    aa.insert(50)
    aa.insert(29)
    
    aa.preorder(aa.root)
    print()
    aa.inorder(aa.root)
    print()
    aa.postorder(aa.root)
    print()