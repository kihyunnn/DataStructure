"""
다음 빈칸(block)을 채워 아래 두 함수(selection_sort, insertion_sort)를 완성하시오.

1) selection_sort
    값 오름차순으로 정렬
2) insertion_sort
    값 오름차순으로 정렬
"""

def selection_sort(arr):
    n = len(arr)
    # i가 0부터 n-1까지 순회하도록 range 완성
    for i in range(n-1):
        min_idx = i
        for j in range(i + 1, n):
            if(arr[j]<arr[min_idx]):
                min_idx = j
            # 최소값 인덱스 갱신 로직 구현
            ########################################
            #                block                 #
            ########################################
        # 스왑(swap) 구문 구현
        temp = arr[min_idx]
        arr[min_idx] = arr[i]
        arr[i] = temp
        ''' block '''
    return arr

def insertion_sort(arr):
    n = len(arr)
    # i가 1부터 n-1까지 순회하도록 range 완성
    for i in range(1,n-1):
        key = arr[i]
        j = i - 1
        # key보다 큰 요소를 뒤로 이동시키는 조건 구현
        while j >= 0 and key<arr[j]:
            temp = arr[j]
            arr[j] = key
            arr[i] = temp

            ########################################
            #                block                 #
            ########################################
        # key 삽입 구문 구현
        ''' block '''
    return arr

def main():
    data = [6, 3, 7, 4, 9, 1, 5, 2, 8]
    print("selection_sort:", selection_sort(data.copy()))
    print("insertion_sort:", insertion_sort(data.copy()))

if __name__ == "__main__":
    main()