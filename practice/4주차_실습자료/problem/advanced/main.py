from CookListDeque import CookListDeque
from CircularQueue import CircularQueue
from TableFood import TableFood

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

def predict_food(list: CookListDeque, time: int):
    ''' 3.1) front와 rear를 초기화 시키시오.'''
    front = ###      block      ###
    rear = ###      block      ###
    
    tmp_cooked = None
    
    while time > 0:
        if ### block ###:
            print("조리될 음식 없음.")
            return TableFood(0, "nothing", 0)
        
        ## 음식이 다 조리되지 않았다면,
        else:
            ''' 3.3) 남아있는 음식 주문 리스트의 totaltime들을 1씩 빼준다. '''
            for i in range(### block ###):
                ### block ###
                
            if ### block ###:
                ### block ###
        time -= 1        
        dst = list
    
    return tmp_cooked, dst

def main():
    cooklist = CookListDeque()
    totaltime_cooklist = CookListDeque()

    ''' 2.3) 리스트에서의 조리되어야 하는 각 음식들의 주문들을 cooklist에 add_rear하라.
             hint) cooklist.add_rear(TableFood(1,"food_a", 8))'''
             
    ################################################
    #                                              #
    #                                              #
    #                    block                     #
    #                                              #
    #                                              #
    ################################################)
    
    ''' 2.4) 각 음식들이 조리되는 데 걸리는 시간
             즉, totaltime으로 업데이트된 조리 리스트를 출력하여라.'''
    totaltime_cooklist = ### block ###
    
    predicted, tmp = predict_food(totaltime_cooklist, 28)
    
    ''' 3.6) 28분 뒤 시점을 기준으로 가장 최근에 조리 완료된 음식의 정보를 출력하여라. '''
    print("pred: ")
    print(f"tablenumber: [{### block ###:2}] / foodname: [{### block ###:2}] / totaltime: [{### block ###}]")
    
    ''' 3.7) 28분 뒤 시점을 기준으로 지금 조리되고 있는 음식의 정보를 출력하여라. '''
    print("cooking now: ")
    print(f"tablenumber: [{### block ###:2}] / foodname: [{### block ###:2}] / totaltime: [{### block ###}]")
    
if __name__ == "__main__":
    main()