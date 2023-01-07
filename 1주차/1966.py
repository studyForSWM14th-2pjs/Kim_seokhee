from collections import deque

test_case = int(input())

for i in range(test_case):
    n, m = map(int, input().split())
    arr = deque(list(map(int, input().split())))
    idx = deque(list(range(n)))

    cnt = 0
    # 처음 값이 최대값이면
    while arr:
        if arr[0] == max(arr):
            answer = arr.popleft()
            idx_pop = idx.popleft()
            cnt += 1
            if idx_pop == m:
                print(cnt)

        else:
            arr.append(arr.popleft())
            idx.append(idx.popleft())
