from Student import Student

class StudentStack:
    def __init__(self, max_stack_size=100):
        self.top = -1
        self.data = []
        self.max_stack_size = max_stack_size

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_stack_size - 1

    def push(self, student: Student):
        if self.is_full():
            print("스택 포화 에러")
            return
        self.data.append(student)
        self.top += 1

    def pop(self):
        if self.is_empty():
            print("스택 공백 에러")
            return None
        
        last_element = self.data[self.top]
        self.data = self.data[:self.top]
        self.top -= 1
        return last_element

    def peek(self):
        if self.is_empty():
            print("스택 공백 에러")
            return None
        print("[peek]")
        self.data[self.top].display()
        return self.data[self.top]

    def display(self):
        print(f"[스택 항목수 {self.top + 1}]")
        for student in self.data:
            student.display()
        print()
