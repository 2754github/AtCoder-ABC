K, N = map(int, input().split())
A = list(map(int, input().split()))
D = [0]*N
for i in range(N-1):
    D[i] = A[i + 1] - A[i]
D[N-1] = K+A[0]-A[N-1]
print(sum(D)-max(D))
