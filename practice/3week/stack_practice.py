class ArraySAtack:
    def __init__(self, capacity):
        self.capacity = capac # 스택 용량
        self.array = [None]*self.capacity # 요소 배열
        self.top = -1 # 상단의 인덱스
        
    def isEmpty(self):
        return self.top == -1
    
