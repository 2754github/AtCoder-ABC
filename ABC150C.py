import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

a = 0
b = 0
seq = range(1, N+1, 1)
L = list(itertools.permutations(seq))
for i, l in enumerate(L):
    if P == l:
        a = i
    if Q == l:
        b = i
print(abs(a-b))
