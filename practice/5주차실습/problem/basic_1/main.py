from Node import Node
from LinkedStack import LinkedStack

def main():
    stack = LinkedStack()
    
    ## 1.4) LinkedStack::push()를 이용하여 다음과 같은 데이터 구조를 갖도록 만들어라.
	## -> top부터 출력시킴.
    ## 출력결과:
	## [LinkedStack]
    ## 학번:22221358        이름:인덕이         학과:기계공학과               
    ## 학번:22221357        이름:인뇽이         학과:컴퓨터공학과              
    ## 학번:22221356        이름:최병희         학과:철학과                 
    ## 학번:22221355        이름:최지원         학과:전기공학과               
    ## 학번:22221354        이름:양건모         학과:전자공학과
    
    ################################################
    #                                              #
    #                                              #
    #                    block                     #
    #                                              #
    #                                              #
    ################################################
    student_data = [
    (22221354 ,"양건모","전자공학과"),
    (22221355 ,"최지원","전기공학과"),
    (22221356 ,"최병희","철학과"),
    (22221357 ,"인뇽이","컴퓨터공학과"),
    (22221358 ,"인덕이","기계공학과")
    ]

    for data in student_data:
        s = Node(*data)  
        stack.push(s)

    stack.display()
    
    ## 1.5) 최종적으로 스택의 데이터 구조과 다음과 같이 될 수 있도록 코드를 구현하여라.
	## 출력결과: 
	## [LinkedStack]
    ## 학번:22221358        이름:인덕이         학과:기계공학과               
    ## 학번:22221357        이름:인뇽이         학과:컴퓨터공학과              
    ## 학번:22231396        이름:하텍이1        학과:new1 학과             
    ## 학번:22221356        이름:최병희         학과:철학과                 
    ## 학번:22231397        이름:하텍이2        학과:new2 학과             
    ## 학번:22221355        이름:최지원         학과:전기공학과               
    ## 학번:22231398        이름:하텍이3        학과:new3 학과             
    ## 학번:22221354        이름:양건모         학과:전자공학과

	## hint) 문제는 LinkedStack::num_push()함수를 먼저 구현하시면 쉽게 풀 수 있습니다.
    ################################################
    #                                              #
    #                    block                     #
    #                                              #
    ################################################
    student_data2 = [
    (22231396 ,"하텍이1 ","new1 학과"),
    (22231397 ,"하텍이2 ","new2 학과"),
    (22231398 ,"하텍이3","new3 학과  ")
    ]
    s = Node(*student_data2[2])
    stack.num_push(s,5)
    s = Node(*student_data2[1])
    stack.num_push(s,4)
    s = Node(*student_data2[0])
    stack.num_push(s,3)
    stack.display()
    

if __name__ == "__main__":
    main()