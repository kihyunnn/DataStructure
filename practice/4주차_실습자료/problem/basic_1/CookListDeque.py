import sys

from CircularQueue import CircularQueue
from TableFood import TableFood

def error(str):
    print(str, file = sys.stderr)
    sys.exit(1)

class CookListDeque:
    def __init__(self):
        self.que = CircularQueue()
    
    def add_rear(self, val: TableFood):
        self.que.enqueue(val)
        
    def delete_front(self):
        return self.que.dequeue()
    
    def get_front(self):
        return self.que.peek()
    
    def add_front(self, val: TableFood):
        if not isinstance(val, TableFood):
            error("Error: 덱에는 TableFood 인스턴스만 넣을 수 있습니다.")
        if self.que.is_full():
            error("Error: 덱이 포화상태입니다.")
        else:
            self.que.front = (self.que.front - 1 + self.que.MAX_QUEUE_SIZE) % self.que.MAX_QUEUE_SIZE
            self.que.data[self.que.front] = val

    def delete_rear(self):
        if self.que.is_empty():
            error("Error: 덱이 공백상태입니다.")
        else:
            ret = self.que.data[self.que.rear]
            self.que.rear = (self.que.rear - 1 + self.que.MAX_QUEUE_SIZE) % self.que.MAX_QUEUE_SIZE
            return ret
    
    def get_rear(self):
        if self.que.is_empty():
            error("Error: 덱이 공백상태입니다.")
        else:
            return self.que.data[self.que.rear]
    
    def display(self):
        print("덱의 내용: ")
        max_i = self.que.rear if self.que.front < self.que.rear else self.que.rear + self.que.MAX_QUEUE_SIZE
        for i in range(self.que.front+1, max_i+1):
            idx = i % self.que.MAX_QUEUE_SIZE
            print(f"tablenumbor: [{self.que.data[idx].tablenumber:2}] / foodname: [{self.que.data[idx].foodname}] / totaltime: [{self.que.data[idx].totaltime:2}]")