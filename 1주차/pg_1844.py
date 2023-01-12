from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def solution(maps):
    row = len(maps)  # 행 길이
    col = len(maps[0])  # 열 길이

    # visited 판별을 위한 maps와 크기가 같은 배열.
    # 방문 안했으니까 모두 0으로 설정
    # 방문하면 1
    visited = [[0 for _ in range(col)]for s in range(row)]

    q = deque()
    q.append((0, 0))
    # 첫 노드는 방문
    visited[0][0] = 1

    # BFS시작
    while len(q):
        r, c = q.popleft()
        for i in range(4):
            nr = r+dx[i]
            nc = c+dy[i]
            if nr < 0 or nr >= row or nc < 0 or nc >= col:
                continue
            if maps[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c]+1

    if visited[row-1][col-1] == 0:
        return -1
    return visited[row-1][col-1]
