import numpy as np


N = int(input())
X = np.array(list(map(int, input().split())))


def calc(x):
    return x**2


ans = float('inf')
for P in range(max(X)+1):
    ans = min(ans, sum(map(calc, X - np.array([P] * N))))
print(ans)
