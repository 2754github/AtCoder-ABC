A, B, X = map(int, input().split())
inf = 0
sup = 1000000000
N = 1000000000
while True:
    dN = len(str(N))
    p = A*N+B*dN
    if p <= X:
        inf = N
    else:
        sup = N
    if abs(sup-inf) <= 1:
        break
    N = -(-(inf+sup)//2)
print(inf)
