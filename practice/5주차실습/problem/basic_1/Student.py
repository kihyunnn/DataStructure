class Student:
    def __init__(self, id: int, name: str, dept: str):
        self.id = id
        self.name = name
        self.dept = dept
    
    def set(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept
    
    def display(self):
        print(f" 학번:{str(self.id):15s} 이름:{self.name:10s}  학과:{self.dept:20s}")