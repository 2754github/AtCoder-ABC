import numpy as np
N = int(input())
x = [0]*N
y = [0]*N
for i in range(N):
    x[i], y[i] = map(int, input().split())


d = [0]*N*(N-1)
k = 0
for i in range(N):
    for j in range(N):
        if i != j:
            a = np.array([x[i], y[i]])
            b = np.array([x[j], y[j]])
            u = b-a
            d[k] = np.linalg.norm(u)
            k += 1

ans = sum(d)/N
print(ans)
