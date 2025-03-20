from FoodStack import FoodStack
from FoodStack import Food

'''
    	음식순서를 stack에 저장하기
         - 소스 파일을 완성하는 문제이다. 그림에서 보이는, 원하는 동작을 하고자 한다.
         - 문제에 대한 예시 그림 설명이 food_explain.png에 있습니다. 주어진 food_explain.png과 아래의 예시 설명을 보고 문제를 해결하세요.
    	stack_a : A 식당의 밀린 주문 리스트
    	stack_b : B 식당의 밀린 주문 리스트
    	stack_result : A,B 식당에서 조리 후 나오는 음식들의 순서를 저장할 스택
    
    ex) 아래와 같은 주문 리스트가 있을 때, A식당 음식 리스트에 대하여 Food_a0라는 음식이 나오는데 걸리는 시간은 10분이며, 
    	Food_a1의 음식이 나오는데 걸리는 시간은 10분이 지난 17분이다(10+7). 그리고 Fodd_a2 음식이 나오는 데 걸리는 시간은
    	29분(10 + 7 + 12)이다. B식당의 리스트도 이와 같은 원리이다.
    	이러한 스택 구조의 주문 리스트가 있을 때, 결과 출력은 다음과 같다. 
    		stack_result ->
    			 Food[0]: name= Food_b0 
    			 Food[1]: name= Food_a0 
    			 Food[2]: name= Food_b1 
    			 Food[3]: name= Food_a1 
    			 Food[4]: name= Food_b2 
    			 Food[5]: name= Food_a2 
    	이와 같이 stack_result가 두 식당의 음식들에 대해서 조리가 끝나는 순서들을 반영할 수 있도록 알고리즘을 구현하여라.
'''

def main():
    stack_a = FoodStack()
    stack_b = FoodStack()
    stack_result = FoodStack()
    
    ## a식당의 음식 주문 리스트 세팅
    stack_a.push(Food("Food_a2", 12))
    stack_a.push(Food("Food_a1", 7))
    stack_a.push(Food("Food_a0", 10))
    
    ## b식당의 음식 주문 리스트 세팅
    stack_b.push(Food("Food_b2", 6))
    stack_b.push(Food("Food_b1", 9))
    stack_b.push(Food("Food_b0", 4))
    
    stack_a.display()
    stack_b.display()
    
    ## Food 데이터를 임시 저장하기 위한.
    c = Food()
    
    ## 두 스택이 모두 비워지지 않았을 때까지 반복
    while not (###  block  ###): 
        ## 한 쪽 식당의 음식의 조리가 모두 끝났다면, 다른 식당의 음식만 순서대로 나오면 됨.
        if stack_b.isEmpty():
            stack_result.push(###  block  ###)
        elif stack_a.isEmpty():
            stack_result.push(###  block  ###)
        
        ## 두 식당 모두 음식 조리가 끝나지 않았다면,
        else:
            ## 각 식당에서 지금 나와야 할 두 음식 중 누가 먼저 나오나?
            if stack_a.peek().time <= ###  block  ###: ## a 식당의 음식이 먼저 나온다면,
                c = stack_b.pop()
                stack_b.push(Food(c.name, (###  block  ###)))
                stack_result.push(###  block  ###)
            else:                                      ## b 식당의 음식이 먼저 나온다면,
                c = stack_a.pop()
                stack_a.push(Food(c.name, (###  block  ###)))
                stack_result.push(###  block  ###)
    
    stack_result.display()
    
if __name__ == "__main__":
    main()