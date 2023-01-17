import sys
input = sys.stdin.readline

n = int(input())


def find(n):
    if n == 0:
        return 0
    a, b = 0, 1
    for i in range(50):
        a, b = b, a+b
        if b > n:
            arr.append(a)
            return find(n-a)


for i in range(n):
    number = int(input())
    arr = []
    find(number)
    arr.sort()
    print(*arr)
