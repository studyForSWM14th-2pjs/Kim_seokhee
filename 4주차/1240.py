# 4 2
# 2 1 2
# 4 3 2
# 1 4 3
# 1 2
# 3 2

import sys
from collections import deque


input = sys.stdin.readline

n, m = map(int, input().split())

# bfs


def bfs(start, end):
    q = deque()
    q.append((start, 0))

    # visited
    visited = [0] * (n+1)
    visited[start] = 1

    while q:
        arrive_point, weight = q.popleft()

        if arrive_point == end:
            return weight

        for next_node, w in graph[arrive_point]:
            if not visited[next_node]:
                visited[next_node] = 1
                q.append((next_node, weight+w))


# 그래프 연결
graph = [[]for _ in range(n+1)]
for i in range(n-1):
    n1, n2, w = map(int, input().split())
    graph[n1].append((n2, w))
    graph[n2].append((n1, w))

for i in range(m):
    start, end = map(int, input().split())
    print(bfs(start, end))
