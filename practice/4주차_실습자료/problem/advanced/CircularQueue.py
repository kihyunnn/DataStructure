import sys

from TableFood import TableFood

MAX_QUEUE_SIZE = 100

def error(str):
    print(str, file = sys.stderr)
    sys.exit(1)

class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.MAX_QUEUE_SIZE = MAX_QUEUE_SIZE
        self.data = [None] * self.MAX_QUEUE_SIZE
    
    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return (self.rear+1) % self.MAX_QUEUE_SIZE == self.front
    
    def enqueue(self, val: TableFood):
        if not isinstance(val, TableFood):
            error("Error: 큐에는 TableFood 인스턴스만 넣을 수 있습니다.")
        if self.is_full():
            error("Error: 큐가 포화상태입니다.")
        else:
            self.rear = (self.rear + 1) % self.MAX_QUEUE_SIZE
            self.data[self.rear] = val
            
    def dequeue(self):
        if self.is_empty():
            error("Error: 큐가 공백 상태입니다.")
        else:
            self.front = (self.front + 1) % self.MAX_QUEUE_SIZE
            return self.data[self.front]
        
    def peek(self):
        if self.is_empty():
            error("Error: 큐가 공백 상태입니다.")
        else:
            return self.data[(self.front+1) % self.MAX_QUEUE_SIZE]
    
    def display(self):
        print("큐의 내용: ", end='')
        max_i = self.rear if self.front < self.rear else self.rear + self.MAX_QUEUE_SIZE
        for i in range(self.front+1, max_i+1):
            print(f"[{self.data[i % self.MAX_QUEUE_SIZE]}]", end='')
        print()