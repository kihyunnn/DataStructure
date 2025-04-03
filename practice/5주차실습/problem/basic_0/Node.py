class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
    
    def getLink(self):
        return self.next
    
    def setLink(self, next):
        self.next = next
    
    def display(self):
        print(f"<{self.data}>")