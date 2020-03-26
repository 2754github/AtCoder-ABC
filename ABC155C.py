import collections

N = int(input())
S = []
for _ in range(N):
    S.append(input())

C = collections.Counter(S).most_common()
M = C[0][1]

ans = []
for c in C:
    if c[1] == M:
        ans.append(c[0])
    else:
        break

ans.sort()
for a in ans:
    print(a)
