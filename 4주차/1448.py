import sys
input = sys.stdin.readline

total = int(input())

arr = []
for i in range(total):
    arr.append(int(input()))

# 내림차순 정렬
arr.sort(reverse=True)

check = 1

# 내림차순으로 정렬했을 때,arr[i]>arr[i+1]+arr[i+2]가 성립이 안된다면 다음 건 볼 것도 없다.
for i in range(len(arr)-2):
    if (arr[i] < arr[i+1]+arr[i+2]):
        print(arr[i] + arr[i+1]+arr[i+2])
        check = 1
        break
    check = -1

if check == -1:
    print(-1)
