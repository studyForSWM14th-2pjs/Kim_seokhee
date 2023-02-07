import sys
import heapq
input = sys.stdin.readline


total = int(input())
for i in range(total):
    max_heap = []
    min_heap = []
    visit = [False] * 1_000_001

    n = int(input())

    for key in range(n):
        line = input().rsplit()
        if line[0] == 'I':
            heapq.heappush(min_heap, (int(line[1]), key))
            heapq.heappush(max_heap, (int(line[1]) * -1, key))
            visit[key] = True

        elif line[0] == 'D':
            if line[1] == '-1':
                # visit이 False일떄 => 삭제된 상태
                # 상대힙에서 삭제된 상태면 버림.
                while min_heap and not visit[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                # 내꺼 처리
                if min_heap:
                    visit[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif line[1] == '1':
                # 상대힙에서 삭제된 상태면 버림.
                while max_heap and not visit[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                # 내꺼 처리
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
    # 쓰레기 노드 처리
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
