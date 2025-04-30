"""
다음 빈칸(block)을 채워 아래 함수들을 완성하시오.

1) selection_sort
    값 오름차순으로 정렬
2) insertion_sort
    값 오름차순으로 정렬
3) frequency_based_selection_sort    
    빈도 내림차순 우선 · 값 오름차순
4) frequency_based_insertion_sort    
    빈도 내림차순 우선 · 값 오름차순
"""

def frequency_calculation(arr):
    # 빈도 계산
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq


def selection_sort(arr):
    n = len(arr)
    # i가 0부터 n-1까지 순회하도록 range 완성
    for i in range(''' block '''):
        min_idx = i
        for j in range(i + 1, n):
            # 최소값 인덱스 갱신 로직 구현
            ########################################
            #                block                 #
            ########################################
        # 스왑(swap) 구문 구현
        ''' block '''
    return arr

def insertion_sort(arr):
    n = len(arr)
    # i가 1부터 n-1까지 순회하도록 range 완성
    for i in range(''' block '''):
        key = arr[i]
        j = i - 1
        # key보다 큰 요소를 뒤로 이동시키는 조건 구현
        while j >= 0 and ''' block ''':
            ########################################
            #                block                 #
            ########################################
        # key 삽입 구문 구현
        ''' block '''
    return arr


def frequency_based_selection_sort(arr):
    freq = frequency_calculation(arr)
    n = len(arr)
    # i가 0부터 n-1까지 순회하도록 range 완성
    for i in range(''' block '''):
        best = i
        # j가 i+1부터 n-1까지 순회하도록 range 완성
        for j in range(''' block '''):
            # 빈도 내림차순 우선 · 값 오름차순 조건 기준으로 best 갱신 로직 구현
            ########################################
            #                block                 #
            ########################################
        # 스왑 구문 구현
        ''' block '''
    return arr

def frequency_based_insertion_sort(arr):
    freq = frequency_calculation(arr)
    n = len(arr)
    # i가 1부터 n-1까지 순회하도록 range 완성
    for i in range(''' block '''):
        key = arr[i]
        j = i - 1
        # 빈도 내림차순 우선 · 값 오름차순 조건 기준으로 삽입 위치 찾기
        while j >= 0 and (''' block '''):
            ########################################
            #                block                 #
            ########################################
        # key 삽입 구문 구현
        ''' block '''
    return arr

def main():
    data = [6, 3, 3, 5, 5, 5, 2, 2, 2, 2, 1, 1, 1]
    print("selection_sort:", selection_sort(data.copy()))
    print("insertion_sort:", insertion_sort(data.copy()))
    print("frequency_based_selection_sort:", frequency_based_selection_sort(data.copy()))
    print("frequency_based_insertion_sort:", frequency_based_insertion_sort(data.copy()))

if __name__ == "__main__":
    main()