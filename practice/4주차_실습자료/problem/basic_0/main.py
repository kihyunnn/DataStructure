from CircularQueue import CircularQueue

'''
    기본 "CircularQueue.py"를 이용하여 원하는 데이터 구조 완성하기
    - "CircularQueue.py" 파일의 'CircularQueue'는 원형큐 구조를 나타내는 클래스이다.
    - 처음 front와 rear의 index는 0으로 초기화되어있다.
    - 아래와 같이 처음 선언된 원형 큐에 대해 연속으로 1~9까지의 수를 enqueue한다.
    - basic_0_explain.png에 있는 데이터 구조를 만들고자 한다.
    - block 안을 채워 나머지 source 코드를 완성하여라
    - 1)은 아래의 block을 채우는 것이며, 2)는 "CircularQueue.py"에 있는 'MAX_QUEUE_SIZE'의 수를 정해주는 것이다.
'''


def main():
    que = CircularQueue()
    
    for i in range(1, 10):
        que.enqueue(i)
        
        
        
    que.display()
    
    ''' 1) 원형큐가 basic_0_explain.png에서 보여지는 데이터들을 갖도록 하시오.'''
    ################################################
    #                                              #
    #                                              #
    #                    block                     #
    #                                              #
    #                                              #
    ################################################
    que.dequeue()
    que.dequeue()
    que.enqueue(10)
    que.enqueue(11)
    que.enqueue(12)

    que.enqueue(13)
    que.enqueue(14)
    
    
    
    que.display()
    
if __name__ == "__main__":
    main()