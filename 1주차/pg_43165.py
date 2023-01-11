def DFS(n, order, numbers, target):
    if (order == len(numbers)-1):
        if (target == n):
            return 1
        else:
            return 0
    return DFS(n+numbers[order+1], order+1, numbers, target) + DFS(n-numbers[order+1], order+1, numbers, target)


def solution(numbers, target):

    answer = DFS(numbers[0], 0, numbers, target) + \
        DFS(-numbers[0], 0, numbers, target)
    return answer
