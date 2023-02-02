import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt = 1


def bfs():
    global cnt
    queue = set([(0, 0, graph[0][0])])

    while queue:
        x, y, z = queue.pop()

        # 말이 지날 수 있는 최대의 칸 초기화
        cnt = max(cnt, len(z))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in z:
                queue.add((nx, ny, graph[nx][ny] + z))


r, c = map(int, input().split())

graph = [list(map(str, input().strip()))for _ in range(r)]


bfs()
print(cnt)
