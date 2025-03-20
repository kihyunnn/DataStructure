from ArrayStack import ArrayStack

"""
    기본 Stack 구조 완성하기
    - 기본 stack 구조를 완성하는 문제이다. "ArrayStack.h"헤더 파일의 'ArrayStack'은 스택 구조를 나타내는 클래스이다. 
    - 강의자료와 달리 ArrayStack의 top의 초기값은 0이다. (강의자료에서의 top 초기값은 -1) 
    - isEmpty() 함수 : 스택이 비웠다면 1을 반환한다. 
    - isFull() 함수 : 스택이 다 찼다면 1을 반환한다. 
    - push() 함수 : 현재 해당 스택에 대해서 데이터 push.
    - pop() 함수 : 현재 해당 스택에 대해서 데이터 pop.
    - peek() 함수 : 현재 해당 스택의 peek 반환.
"""
def main():
    stack = ArrayStack()
    
    for i in range(10):
        stack.push(i)
        
    stack.display()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.display()
    
    print(f"현재의 peek : {stack.peek()}")
    
if __name__ == "__main__":
    main()