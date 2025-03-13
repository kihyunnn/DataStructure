

###############################################################
#                   피라미드 모양의 배열 만들기                    #
###############################################################

ARRAY_ROWS = 6
ARRAY_COLS = ARRAY_ROWS * 2


def main():
    ''' -------------------------------------------------------------------------
    
        Problem 1. 주어진 2차원 배열이 아래와 같이 정렬된 원소들을 갖도록 하는 코드를 구현하시오.
        - 이중 for문을 사용할 것.

        ex) array[[6][12]]
        
            1열 2열 3열 4열 5열 6열 7열 8열 9열 10열 11열
        1행                     *
        2행                 *   *   *
        3행             *   *   *   *   *   
        4행         *   *   *   *   *   *   *   
        5행     *   *   *   *   *   *   *   *   *   
        6행 *   *   *   *   *   *   *   *   *   *   *
        
        출력 결과
        ->
              *     
             ***    
            *****   
           *******  
          ********* 
         ***********
         
    ------------------------------------------------------------------------- ''' 
    
    array = [[' ' for _ in range(ARRAY_COLS)] for _ in range(ARRAY_ROWS)]

    for i in range(ARRAY_ROWS):
        ##########################
        #                        #
        #                        #
        #          block         #
        #                        #
        #                        #
        ##########################
        start = ARRAY_ROWS - i  # 시작 위치
        end = ARRAY_ROWS+ i + 1  # 끝 위치
        for j in range(start, end):
            array[i][j] = '*'
            
            
    for row in array: # 출력
        print(''.join(row)) # 배열을 문자열로 출력
         
if __name__ == "__main__":
    main()