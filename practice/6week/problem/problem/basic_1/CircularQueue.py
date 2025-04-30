from BinaryNode import *

MAX_QUEUE_SIZE = 100

class CircularQueue:
    def __init__(self):
        self.data = [None for i in range(MAX_QUEUE_SIZE)]
        self.front = self.rear = 0
    def isEmpty(self)->bool:
        return self.front == self.rear
    def isFull(self)->bool:
        return (self.rear+1) % MAX_QUEUE_SIZE == self.front
    def enqueue(self, n: BinaryNode):
        if self.isFull():
            print("Error: 큐가 포화상태입니다.")
        else:
            self.rear = (self.rear+1) % MAX_QUEUE_SIZE
            self.data[self.rear] = n
    def dequeue(self)->BinaryNode:
        if self.isEmpty():
            print("Error: 큐가 공백상태입니다")
        else:
            self.front = (self.front+1) % MAX_QUEUE_SIZE
            return self.data[self.front]
        return None