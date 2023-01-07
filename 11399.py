# 5
# 3 1 4 3 2


n = int(input())

arr = []
arr = list(map(int, input().split()))

arr.sort()
answer = 0
for i in range(len(arr)):
    answer += sum(arr[0:i+1])
print(answer)
