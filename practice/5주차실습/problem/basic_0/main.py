from Node import Node
from LinkedQueue import LinkedQueue

'''
    "LinkedQueue.py"이용하여 문제에서 원하는 LinkedQueue 데이터 구조 만들기.
    - "LinkedQueue.h"에서 class 'LinkedQueue'는 교재의 "Node.py"에서의 'Node' class를 가지고 있다.  
    - 각 문제에서 원하는 구현이 되도록 모든 block을 채워 넣어라.
'''

def main():
    que = LinkedQueue()
    
    for i in range(1, 10):
        que.enqueue(Node(i))
        
    que.display()
    
    ## 1.4) 이 시점 que은 데이터 구조는 다음과 같음.
	## -> [큐 내용] :  < 1> < 2> < 3> < 4> < 5> < 6> < 7> < 8> < 9>
	## LinkedQueue::dequeue()를 이용하여 다음과 같은 데이터 구조를 갖도록 만들어라.
	## -> [큐 내용] :  < 4> < 5> < 6> < 7> < 8> < 9>
    ################################################
    #                    block                     #
    ################################################
    
    que.display()
    
    ## 1.5) 최종적으로 큐의 데이터 구조과 다음과 같이 될 수 있도록 코드를 구현하여라.
	## 출력결과: [큐 내용] :  < 4> < 6> < 8>
	## hint) 문제는 LinkedQueue::num_dequeue()함수를 먼저 구현하시면 쉽게 풀 수 있습니다.
    ################################################
    #                    block                     #
    ################################################
    
    que.display()
    
if __name__ == "__main__":
    main()