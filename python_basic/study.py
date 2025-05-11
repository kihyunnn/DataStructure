n = 5
arr = [0]*5
for i in range(5):
    arr[i]=int(input())

#insertino sortin 오름차순

for i in range(1,n):
    key = arr[i]
    j = i-1
    while j>=0 and arr[j]>key:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = key
    
# 평균 값 구하기
sum  = 0
for i in range(n):
    sum += arr[i]
    
avr = int(sum/n)
# print("---")

# print(arr)
# print("---")
print(avr)
print(arr[2])
