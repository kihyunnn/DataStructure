class ArrayStack:
    def __init__(self, max_stack_size=100):
        self.data = []
        self.top = 0
        self.max_stack_size = max_stack_size
        
    def is_empty(self):
        ''' 1) isEmpty() 함수를 마저 작성하시오. '''
        return ###  block  ###
    
    def is_full(self):
        ''' 2) isFull()의 함수를 마저 작성하시오. '''
        return ###  block  ###
    
    def push(self, e):
        if self.is_full():
            print("스택 포화 에러")
            return
        ''' 3) push의 함수를 마저 작성하시오. '''
        #####################################
        #               block               #
        #####################################
    
    def pop(self):
        if self.is_empty():
            print("스택 공백 에러")
            return None
        
        ''' 4) pop의 함수를 마저 작성하시오. '''
        #####################################
        #               block               #
        #####################################
    
    def peek(self):
        if self.is_empty():
            print("스택 공백 에러")
            return None
        
        ''' 5) peek의 함수를 마저 작성하시오. '''
        return ###  block  ###
    
    def display(self):
        print(f"[스택 항목의 = {self.top}] ==> ", end="")
        
        ''' 6) test의 결과를 보고, 올바른 출력이 나올 수 있도록 for문을 완성하시오. '''
        for ###  block  ###:
            print(f"data[{i}]: {self.data[i]} ", end="")
        print()