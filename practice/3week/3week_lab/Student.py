class Student:
    def __init__(self, id, name, dept):
        self.set(id, name, dept)
        
    def set(self, id, name, dept):
        self.id = id
        self.name = name
        self.dept = dept
        
    def display(self):
        print(f" 학번:{self.id:<15} 성명:{self.name:<10} 학과:{self.dept:<20}")