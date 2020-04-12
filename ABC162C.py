import math
from functools import reduce
import itertools


def gcd(*numbers):
    return reduce(math.gcd, numbers)


K = int(input())
l = list(range(1, K + 1))
ans = K * (K + 1) // 2
for i in itertools.combinations(l, 2):
    ans += 3*(gcd(i[0], i[0], i[1])+gcd(i[0], i[1], i[1]))
for i in itertools.combinations(l, 3):
    ans += 6*gcd(i[0], i[1], i[2])

print(ans)
