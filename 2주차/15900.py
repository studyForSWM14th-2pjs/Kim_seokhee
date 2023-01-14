# DFS => 어떤 노드를 방문했었는지 여부를 반드시 검사 해야 한다.
# 넓이보다 깊이 우선 탐색
# 그렇지 않을 경우 무한루프에 빠질 위험이 있다.
# pypy로 제출함.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

# 만약 4라면,
n = int(input())

# 0 1 2 3 4
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
distance = [0 for _ in range(n+1)]

for i in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(cur):
    # 방문했고
    visited[cur] = True
    for next in graph[cur]:
        # 방문 안했으면,
        if visited[next] == False:
            # distance에는 루트노드부터 모든 노드까지에 거리를 갱신해준다.
            distance[next] = distance[cur] + 1
            dfs(next)


dfs(1)

answer = 0
# 리프노드만 찾아서 하면된다.
for i in range(2, n+1):
    # 리프노드는 연결 된 노드가 하나.
    if len(graph[i]) == 1:
        answer += distance[i]

if answer % 2 == 0:
    print("No")
else:
    print("Yes")
