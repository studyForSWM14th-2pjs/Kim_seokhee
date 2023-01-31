import sys
imput = sys.stdin.readline

n = int(input())

u = set()
for i in range(n):
    u.add(int(input()))

print(u)

a_b_sums = set()
for i in u:
    for j in u:
        a_b_sums.add(i + j)

ans = set()
for i in u:
    for j in u:
        if (i - j) in a_b_sums:
            ans.add(i)

sorted_ans = sorted(ans)
print(sorted_ans[-1])
