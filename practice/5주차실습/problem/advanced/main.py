from TableFood import TableFood
from Node import Node
from LinkedQueue import LinkedQueue

'''
    "LinkedQueue.h"를 이용하여 식당에서의 음식 주문표 알고리즘 구현하기.
    - "LinkedQueue.h"에서 class 'LinkedQueue'는 교재의 예제와 같은 "Node.h"에서의 'Node' class를 가지고 있다. 
 	- "Node" class의 매개변수로는 기존 자료형이 아닌, 구조체 'TableFood'를 매개변수로 취하고 있다. -> 구조체 'TableFood'은 "TableFood.py"에 정의되어 있다.
 	- advanced_explain.pdf에 있는 그림의 알고리즘을 구현하고자 한다. block안을 채워 나머지 source 코드를 완성하여라. 
 	- advanced_explain.pdf에 대한 설명:
 		->  어떤 4개의 table이 있는 식당에서 "LinkedQueue.py" 활용하여, total time 조리 주문표를 만들고자 한다. 
 			또한, 추가적으로, front를 기준으로 원하는 순서 번째의 음식을 주문 취소하고자 한다.
 			
	각 문제에서 원하는 구현이 되도록 모든 block을 채워 넣어라.
'''

def totaltime_list(que: LinkedQueue):
    sum = 0
    temp = que.peek()
    
    ## 3.3) 리스트에서의 조리되어야 하는 각 음식들의 현재 time들을 각 음식들의 조리가 완료되는 total time으로 업데이트 하여라. 
    while temp != None:
        sum += que.data.## block ##
        temp.data.totaltime = sum
        temp = ## block ##
        
def delete_foodlist(que: LinkedQueue, num: int):
    deletefood_time = None # 이번에 제거하고자 하는 음식의 조리완료까지 걸리는 totaltime
    
    ## 3.4) delete_food : 이번에 제거 하고자 하는 음식
    delete_food = ## block ##
    
    ## temp : 현재 조리리스트에서 delete_food 이후로 조리 완료되는 음식들의 totaltime 조정을 위한.
    temp = que.num_peek(num).getLink()
    
    ## 3.5) 이번에 제거 하고자 하는 음식이 "food_a"이면 ~
    if delete_food.data.foodname == ## block ##:
        deletefood_time = 8
    elif delete_food.data.foodname == ## block ##:
        deletefood_time = 12
    elif delete_food.data.foodname == ## block ##:
        deletefood_time = 9
    
    ## 3.6) delete_food가 제거된다면, delete_food 이후로 조리 완료되는 
    ## 음식들은 totaltime을 delete_food가 조리되는 시간만큼빼줘야한다.
    while temp != None:
        ## block ##
        temp = temp.getLink() 
    
    ## block ##

def main():
    cooklist = LinkedQueue()
    
    ## 3.8) 리스트에서의 조리되어야 하는 각 음식들의 주문들을 다음과 같은 데이터 구조 상태가 되도록 cooklist에 enqueue하라.
    ## -> front부터 출력시킨 것임.
    ## [큐 내용] : 
    ##  table_num: < 1> / foodname: <food_a> / time: < 8> 
    ##  table_num: < 1> / foodname: <food_b> / time: <12> 
    ##  table_num: < 3> / foodname: <food_a> / time: < 8> 
    ##  table_num: < 2> / foodname: <food_c> / time: < 9> 
    ##  table_num: < 4> / foodname: <food_a> / time: < 8> 
    ##  table_num: < 4> / foodname: <food_b> / time: <12>
    
    ################################################
    #                                              #
    #                                              #
    #                    block                     #
    #                                              #
    #                                              #
    ################################################
    cooklist.display()
    
    ## 3.8) 
    ## delete_foodlist을 이용하여 다음과 같은 데이터 구조 상태가 될 수 있도록 코드를 구현하여라.
    ## -> front부터 출력시킨 것임.
    ## [큐 내용] : 
    ##  table_num: < 1> / foodname: <food_a> / time: < 8> 
    ##  table_num: < 3> / foodname: <food_a> / time: <16> 
    ##  table_num: < 2> / foodname: <food_c> / time: <25> 
    ##  table_num: < 4> / foodname: <food_a> / time: <33> 
    ##  table_num: < 4> / foodname: <food_b> / time: <45>
    
    totaltime_list(cooklist)
    ## block ##
    cooklist.display()
    
if __name__ == "__main__":
    main()