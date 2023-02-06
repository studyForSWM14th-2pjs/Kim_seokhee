# 연속된 합 중에서 최대 구하라!

# 계속 합칠래, 새로 갱신할래?
# 다음 인덱스의 숫자가 계속 합쳐온 숫자에 더해졌을 때 더 크냐, 아니면 자기 혼자가 더 크냐의 싸움

import sys
input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))

answer = [num_list[0]]
for i in range(len(num_list)-1):
    answer.append(max(num_list[i+1]+answer[i], num_list[i+1]))
print(max(answer))
