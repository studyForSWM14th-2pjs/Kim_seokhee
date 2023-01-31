# 크루스칼 알고리즘
# 1. 간선들을 정렬
# 2. 간선이 잇는 두 정점의 부모를 찾는다.
# 3. 다르다면 하나의 부모를 바꾸어 연결 시켜준다.

# Kruskal알고리즘은 간선들을 정렬해야하기 때문에 간선이 적으면 Kruskal,
# 많으면 Prim을 선택한다.

import sys
input = sys.stdin.readline

V, E = map(int, input().split())

# parents 노드
parent = [i for i in range(V+1)]


Earr = []
for i in range(E):
    Earr.append(list(map(int, input().split())))

# 간선 오름차순
Earr.sort(key=lambda x: x[2])

# 부모 찾는 함수


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


# 3 3
# 1 2 1
# 2 3 2
# 1 3 3

# 1 2 3
# 1 1 3
answer = 0
for a, b, weight in Earr:
    roota = find(a)  # 1
    rootb = find(b)  # 3
    # 부모가 다르면 작은 값으로 연결하기
    if (rootb != roota):
        if (roota > rootb):
            parent[roota] = rootb
        else:
            parent[rootb] = roota
        answer += weight
    # if (parent_a > parent_b):
    #     parent[a] = parent[b]
    #     answer += weight
    # elif (parent_b > parent_a):
    #     parent[b] = parent[a]
    #     answer += weight


print(answer)
