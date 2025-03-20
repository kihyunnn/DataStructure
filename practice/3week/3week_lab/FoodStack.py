class Food:
    def __init__ (self, name="", time=0):
        self.set(time, name)
        
    def set(self, time, name):
        self.time = time
        self.name = name
        

class FoodStack:
    def __init__(self, max_stack_size=100):
        self.food = []
        self.top = 0
        self.max_stack_size = max_stack_size
        
    def isEmpty(self):
        return self.top == 0
    
    def isFull(self):
        return self.top == self.max_stack_size
    
    def push(self, e: Food):
        if self.isFull():
            print("스택 포화 에러")
            return

        self.food.append(e)
        self.top += 1
        
    def pop(self):
        if self.isEmpty():
            print("스택 공백 에러")
            return None
        
        self.top -= 1
        last_element = self.food[self.top]
        self.food = self.food[:self.top]
        
        return last_element
    
    def peek(self):
        if self.isEmpty():
            print("스택 공백 에러")
            return None
        return self.food[-1]
    
    def display(self):
        print(f"[스택 항목의 = {self.top}] ==> ")
        for i, f in enumerate(self.food):
            print(f"Food[{i}]: name= {f.name}")
        print()
    
    