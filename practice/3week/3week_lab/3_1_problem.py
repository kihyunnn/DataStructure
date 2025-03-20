from ArrayStackStudent import StudentStack
from Student import Student

'''
    - 소스 파일을 완성하는 문제이다. 두 스택을 선언하여, 원하는 동작을 하고자 한다.
    - 문제가 explain.png에 있습니다. 주어진 explain.png를 보고 문제를 해결하시오.
    
    result ->
        [스택 항목수 1]
        학번:20240320        성명:양건모        학과:전기컴퓨터공학과 
        
        [스택 항목수 2]
        학번:20240322        성명:모건양        학과:전기컴퓨터공학과            
        학번:20240321        성명:건모양        학과:전기컴퓨터공학과 
'''

def main():
    stack1 = StudentStack()
    stack2 = StudentStack()
    
    geonmo = Student(22221534, "양건모", "전기컴퓨터공학과")
    moyang = Student(22231534, "건모양", "전기컴퓨터공학과")
    geonyang = Student(22241534, "모건양", "전기컴퓨터공학과")
    
    
    ##  1) explain.png에서 보여지는 알고리즘을 구현하시오. 
        ##########################
        #                        #
        #                        #
        #          block         #
        #                        #
        #                        #
        ##########################
    stack1.push(geonmo)
    stack1.push(moyang)
    stack1.push(geonyang)
    stack2.push(stack1.pop())
    stack2.push(stack1.pop())
    
    stack1.display()
    stack2.display()
    
if __name__ == "__main__":
    main()