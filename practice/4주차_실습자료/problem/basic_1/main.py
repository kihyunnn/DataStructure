from CookListDeque import CookListDeque
from CircularQueue import CircularQueue
from TableFood import TableFood

'''
    "CookListDeque.py"를 이용하여 식당에서의 음식 주문표 알고리즘 구현하기.
    
        - "CookListDeque.py"에서 class 'CookListDeque'는 basic0 문제에서와 같은 
           원형 큐 클래스 'CircularQueue'를 포함하고 있으며, 'data'에는 'TableFood' 클래스의 객체가 들어간다. 
           -> 'TableFood'는 "TableFood.py"에 정의되어 있다. 
           
        - 처음 front와 rear의 index는 0으로 초기화되어 있다. 
        
        - basic_1_explain.png에 있는 그림의 알고리즘을 구현하고자 한다. block안을 채워 나머지 source 코드를 완성하여라.
        
        -  basic_1_explain.png에 대한 설명:
  			->  어떤 4개의 table이 있는 식당에서 Deque를 활용하여, basic1와 같이 total time 조리 주문표를 만들고자 한다.

            [1]	totaltime_list : 각 음식이 조리가 완료되는 시간으로 time update해주는 함수.
        
        각 문제에서 원하는 구현이 되도록 모든 block을 채워 넣어라.
'''

def totaltime_list(list: CookListDeque):
    sum = 0 
    
    ''' 2.1) front와 rear를 초기화 시키시오. (hint: CookListDeque.py)'''
    front = (list.que.front + 1 + list.que.MAX_QUEUE_SIZE) % ### block ###
    rear = ###      block      ###
    
    ''' 2.2) 리스트에서의 조리되어야 하는 각 음식들의 현재 time들을 각 음식들의
             조리가 완료되는 totaltime으로 업데이트 하여라 '''
    for i in range(front, rear+1):
        sum += ### block ###
        list.que.data[i%list.que.MAX_QUEUE_SIZE].totaltime = sum
        
    return list

def main():
    cooklist = CookListDeque()
    totaltime_cooklist = CookListDeque()
    
    ''' 2.3) 리스트에서의 조리되어야 하는 각 음식들의 주문들을 cooklidat에 add_rear 하여라. 
             hint) cooklist.add_rear(TableFood(1, "food_a", 8))'''
             
    ################################################
    #                                              #
    #                                              #
    #                    block                     #
    #                                              #
    #                                              #
    ################################################
    
    ''' 2.4) 각 음식들이 조리되는 데 걸리는 시간
             즉, totaltime으로 업데이트된 조리 리스트를 출력하여라.'''
    totaltime_cooklist = ### block ###
    totaltime_cooklist.display()
    
if __name__ == "__main__":
    main()