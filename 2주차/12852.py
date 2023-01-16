# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.

import sys
input = sys.stdin.readline

n = int(input())

dp = [[0, []] for _ in range(n + 1)]  # [최솟값, 경로 리스트]
dp[1][0] = 0  # 최솟값
dp[1][1] = [1]  # 경로를 담을 리스트

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0]+1
    dp[i][1] = dp[i-1][1]+[i]
    if i % 3 == 0 and dp[i//3][0]+1 < dp[i][0]:
        dp[i][0] = dp[i//3][0]+1
        dp[i][1] = dp[i//3][1]+[i]
    if i % 2 == 0 and dp[i//2][0]+1 < dp[i][0]:
        dp[i][0] = dp[i//2][0]+1
        dp[i][1] = dp[i//2][1]+[i]

print(dp[n][0])
for i in dp[n][1][::-1]:  # 뒤집은 뒤 출력
    print(i, end=' ')
