# a=list(input()) 하면 ...##. => ['.','.','.','#','#','.','/n'] 이렇게 받아진다.
# 맨뒤 에 공백을 없애자 a=list(input().strip()) 양 옆의 공백을 없애준다. => ['.','.','.','#','#','.']

from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]


def BFS(o, v):
    q = deque([(o, v)])
    to, tv = 0, 0
    while q:
        x, y = q.popleft()
        for i in range(5):
            nx = x+dx[i]
            ny = y+dy[i]
            # 바운더리 안이고 방문한 적이 없으면
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                # 만약 벽이라면,
                if graph[nx][ny] == '#':
                    continue
                # 벽이 아니라면
                if graph[nx][ny] == 'o':
                    to += 1
                if graph[nx][ny] == 'v':
                    tv += 1
                q.append((nx, ny))
                visited[nx][ny] = 1
    return to, tv

# 정답 코드
# if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
#            if graph[nx][ny] == '#':
#                 continue
#             elif graph[nx][ny] == 'v':
#                 tv += 1
#             elif graph[nx][ny] == 'o':
#                 to += 1
#             q.append((nx, ny))
#             visited[nx][ny] = 1

# 내 코드(런타임 에러)
# if 0 <= nx | nx >= row | ny < 0 | ny >= col:
#                 continue
#             # 벽이 아니고 방문하지 않았으면,
#             if graph[nx][ny] != '#' and not visited[nx][ny]:
#                 if graph[nx][ny] == 'o':
#                     to += 1
#                 if graph[nx][ny] == 'v':
#                     tv += 1
#                 q.append((nx, ny))
#                 visited[nx][ny] = 1


graph = []
row, col = map(int, input().split())
visited = [[0 for _ in range(col)]for s in range(row)]

# graph에 받기,
for i in range(row):
    temp = list(input().strip())
    graph.append(temp)

sheep, wolf = 0, 0
BFS_wolf, BFS_sheep = 0, 0
for i in range(row):
    for j in range(col):
        if not visited[i][j] and graph[i][j] != '#':
            BFS_sheep, BFS_wolf = BFS(i, j)
            if BFS_sheep > BFS_wolf:
                sheep += BFS_sheep
            else:
                wolf += BFS_wolf

print(sheep, wolf)
