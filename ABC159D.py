import collections
N = int(input())
A = list(map(int, input().split()))

Cntr = collections.Counter(A)
Sum = 0
for c in Cntr.items():
    key = c[0]
    val = c[1]
    if val > 1:
        Sum += val * (val - 1) // 2

for a in A:
    print(Sum-(Cntr[a]-1))
