from Student import Student
from Node import Node

class LinkedStack:
    def __init__(self):
        self.top = None
        
    def isEmpty(self):
        return self.top == None
    
    def push(self, n: Node):
        if self.isEmpty():
            self.top = n
        else:
            n.setLink(self.top)
            self.top = n
    
    ## top을 기준으로 num번째 stack 공간에 n이라는 노드를 push한다.    
    def num_push(self, n: Node, num: int):
        temp = self.top # num번째 노드의 데이터를 임시로 담는 변수
        temp_before = None # num번째 노드의 이전 노드 
        
        if self.isEmpty():
            self.top = n
        
        ## 1.1) 1번째 노드의 Node에 n을 push 하고자 한다면 ~
        elif num == 1:
            ################################################
            #                    block                     #
            ################################################
        ## 1.2) for문을 통해 num번째 노드 Node를 찾는다.
        else:
            for i in range(## block ##):
                temp_before = temp
                temp = ## block ##
                
                if temp == None:
                    print("index is over.")
                    break
            
            ## 1.3) push될 노드를 고려하여, 스택 링크들 재수정.
            temp_before.## block ##
            n.## block ##
    
    def pop(self):
        if self.isEmpty():
            return None
        
        n = self.top
        self.top = self.top.getLink()
        return n
    
    def peek(self):
        return self.top
    
    def display(self):
        print("[LinkedStack]")
        temp = self.top
        while temp != None:
            temp.display()
            temp = temp.getLink()