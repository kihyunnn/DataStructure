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
        if array[input_index[0]] == '\0':
            return END
        elif array[input_index[0]] == ' ':
            return SPACEzz
    
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
    previous_index = -1
    current_index = [0]
    status_flag = 0 
    
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
        status_flag = isSpace(array, current_index) #
        
        ###########################################
        #                                         #
        #                                         #
        #                  block                  #
        #                                         #
        #                                         #
        ###########################################
        
        if status_flag == END:
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
