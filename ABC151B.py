N, K, M = map(int, input().split())
A = list(map(int, input().split()))
X = max(0, M*N-sum(A))
print(X if X <= K else -1)
