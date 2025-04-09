from TableFood import TableFood

class Node:
    def __init__(self, val: TableFood):
        self.data = val
        self.next = None
    
    def getLink(self):
        return self.next
    
    def setLink(self, next):
        self.next = next
    
    def display(self):
        print(f" table_num: <{self.data.tablenumber:2d}> / foodname: <{self.data.foodname}> / time: {self.data.totaltime:2d}")