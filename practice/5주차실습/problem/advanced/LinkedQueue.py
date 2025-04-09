from Node import Node

class LinkedQueue:
    def __init__(self):
        self.front = None # 가장 먼저 삽입된 노드의 포인터
        self.rear = None # 마지막에 삽입된 노드의 포인터
    
    def isEmpty(self):
        return self.front == None
    
    ## 삽입 연산: 연결된 큐의 맨 뒤에 노드 삽입
    def enqueue(self, n: Node):
        if self.isEmpty():
            self.front = self.rear = n
        else:
            self.rear.setLink(n)
            self.rear = n
    
    ## 삭제 연산: 연결된 큐의 맨 앞 노드를 삭제
    def dequeue(self):
        if self.isEnpty():
            return None
        
        temp = self.front
        self.front = self.front.getLink()
        if self.front == None:
            self.rear = None
        return temp
    
    ## 연결된 큐의 맨앞에서 num번째 노드를 dequeue
    def num_dequeue(self, num: int):
        temp = self.front # dequeue하고자 하는 노드의 데이터를 임시로 담는 변수
        temp_before = None # temp의 전 노드
        
        ## 1.1) 1번째 노드의 Node를 찾고자 한다면 ~
        
        if self.isEmpty():
            return None
        elif num == 1:
            self.front = temp.getLink()
        ## 1.2) for문을 통해 num번째 노드의 Node를 찾는다.
        else:
            for i in range(num-1):
                temp_before = temp
                temp = temp.getLink()
            if temp == None:
                print("index is over.")
                return temp
            
            ## 1.3) dequeue될 노드를 고려하여, 큐 링크들 재수정.
            temp_before.setLink(temp.getLink())
            
        if self.front == None:
            self.rear = None
            
        return temp
        
    def peek(self):
        return self.front
    
    def num_peek(self, num: int):
        if self.isEmpty():
            return None
        
        temp = self.front # dequeue하고자 하는 노드의 데이터를 임시로 담는 변수
        
        ## 3.1) 1번째 노드의 Node를 찾고자 한다면 ~
        if num == 1:
            temp = self.front ## block ##
        
        ## 3.2) for문을 통해 num번째 노드의 Node를 찾는다.
        else:
            for i in range(num-1):
                temp = temp.getLink()
                
            if temp == None:
                print("index is over.")
                return temp
            
            if self.front == None:
                self.rear = None #이게 왜있는지 모르겠
                
        return temp
    
    def display(self):
        print("[큐 내용] : ")
        temp = self.front
        while temp != None:
            temp.display()
            temp = temp.getLink()