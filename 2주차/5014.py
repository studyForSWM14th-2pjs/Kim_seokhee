# 10 1  10 2  1
# F, S, G, U, D

# F=꼭대기 층
# S=현재 위치 층
# G=목적치 층
# U=한 번에 올라갈 수 있는 층
# D=한 번에 내려갈 수 있는 층


from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

# count를 세줄 배열
count = [0]*(F+1)
# 효율을 위한 방문한 노드 재방문 방지
visited = [0]*(F+1)


def BFS(s):
    q = deque()
    q.append(s)
    while q:
        now = q.popleft()
        visited[now] = 1
        # 만약 현재(꺼낸) 층이 목적지라면.
        if (now == G):
            return count[now]
        for i in (now-D, now+U):
            if 0 < i <= F and not visited[i]:
                q.append(i)
                count[i] = count[now]+1
                visited[i] = 1
    if count[G] == 0:
        return "use the stairs"


print(BFS(S))
