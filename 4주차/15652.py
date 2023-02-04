# input
# 4 2

# output
# 1 1
# 1 2
# 1 3
# 1 4
# 2 2
# 2 3
# 2 4
# 3 3
# 3 4
# 4 4
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []


def dfs(start):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(start, n+1):
        arr.append(i)
        dfs(i)
        arr.pop()


dfs(1)
