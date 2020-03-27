N = int(input())
P = list(map(int, input().split()))
cnt = 0
m = N+1
for p in P:
    m = min(m, p)
    if p <= m:
        cnt += 1
print(cnt)
