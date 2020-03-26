N, K = map(int, input().split())
H = list(map(int, input().split()))
H = sorted(H, reverse=True)
del H[:min(N, K)]
print(sum(H))
