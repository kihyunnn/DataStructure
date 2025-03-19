###############################################################
#            주어진 배열 안의 각 단어들을 뒤집어서 출력하기            #
###############################################################


SPACE = 1
END   = 2

##문자열에서 ' 'or'\0'을 찾는 함수. ' 'or'\0'가 있다면 각 문자에 해당하는 상태 값을 반환하며, *input_index를 통해 index 도출
def isSpace(array, input_index):
    
    ''' 
        Problem 1
          함수가 아래 예시와 같은 기능을 할 수 있도록 block을 채워주세요. 
    '''
    while True:
        input_index[0] += 1
        if array[input_index[0]] == '.':
            return END
        elif array[input_index[0]] == ' ':
            return SPACE
    
    ''' -> isspace함수의 이해를 위한 예시:
    
        다음과 같은 코드를 돌렸을 때의 결과. 
        
        def main():
            A = "I am happy today."
            index = [0]
            
            for i in range(A):
                isSpace(A, index)
                print(index)
                
        -> result:
                  [1] [4] [10] [16]
        
    '''
      
## isspace를 이용하여, 문자열 안에서 단어별로 뒤집어서 출력시키는 함수.
def printInverse(array):
    previous_index = -1 # 이전 단어의 index
    current_index = [0] # current_index[0] = 0
    status_flag = 0 # 1: SPACE, 2: END
    
    '''
        Problem 2.
          아래에서 주어진 형식을 재구성 하여도 좋습니다.
          다만, main의 최종 출력 결과가 다음과 같이 나올 수 있도록 코드를 구현해주세요.
        
        -> result:

            A배열 안의 각 단어들을 뒤집어서 출력: 
            I ma yppah yadot 

            B배열 안의 각 단어들을 뒤집어서 출력: 
            eW tnaw ot niw eht tsrif ezirp 
    '''
    while True:
        status_flag = isSpace(array, current_index) # status_flag = 1 or 2이 담기고 current_index[0]는 ' 'or'\0'의 index가 담김
        # print(current_index[0]) 디버깅용 코드
        ###########################################
        #                                         #
        #                                         #
        #                  block                  #
        #                                         #
        #                                         #
        ###########################################
        if status_flag == SPACE: # status_flag가 SPACE일 때
            word = array[previous_index+1:current_index[0]] # word에는 이전 단어의 index+1부터 현재 단어의 index까지의 문자열 즉 단어를 담음
            reversed_word = word[::-1] # reversed_word에는 word를 뒤집은 문자열을 담음 
            print(reversed_word, end = ' ') # reversed_word를 출력하고 띄어쓰기를 함
            previous_index = current_index[0] # previous_index에는 현재 단어의 index를 담음
            
        
        if status_flag == END: # status_flag가 END일 때
            #처음에 여기에 로직을 구현 안했더니 마지막 단어를 뒤집지 못해서 추가. END가 그 때 단어를 뒤집어야 하기 떄문
            #위와 동일한 구조
            word = array[previous_index+1:current_index[0]] 
            reversed_word = word[::-1]
            print(reversed_word, end = ' ')
            previous_index = current_index[0]

            break
        
    print()

## 주어진 배열 안의 각 단어들을 뒤집어서 출력하기 
def main():
    A = "I am happy today."
    B = "We want to win the first prize."
    
    print("A 배열 안의 각 단어들을 뒤집어서 출력: ")
    printInverse(A)
    print()
    
    print("B 배열 안의 각 단어들을 뒤집어서 출력: ")
    printInverse(B)
    print()
    
if __name__ == "__main__":
    main()
