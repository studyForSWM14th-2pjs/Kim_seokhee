# 4 7
# 6 13
# 4 8
# 3 6
# 5 12
# 냅색 알고리즘 - 선택 하느냐, 선택 안하느냐 배낭문제

stuff = [[0, 0]]
N, K = map(int, input().split())

# stuff 채우기
# weight , value
for i in range(N):
    stuff.append(list(map(int, input().split())))

# 배낭 채우기 알고리즘

# 선택 안 할시 위에꺼 그대로 가져와야 하므로 첫번째 줄도 다 0 으로 초기화 해준다.

# (N+1) * (K+1) 배열
arr = [[0 for _ in range(K+1)]for s in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = stuff[i][0]
        value = stuff[i][1]
        if weight <= j:
            # 선택 or 선택 x 중에 max 값
            arr[i][j] = max(value+arr[i-1][j-weight], arr[i-1][j])
        else:
            arr[i][j] = arr[i-1][j]

print(arr[N][K])
