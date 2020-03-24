N, M = map(int, input().split())
if N == 1:
    print(int((M*(M-1))/2))
elif M == 1:
    print(int((N*(N-1))/2))
else:
    print(int((N*(N-1))/2)+int((M*(M-1))/2))
