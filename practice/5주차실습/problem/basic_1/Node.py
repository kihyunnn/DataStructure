from Student import Student

class Node(Student):
    def __init__(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept
        self.next = None
    
    def getLink(self):
        return self.next
    
    def setLink(self, next):
        self.next = next