A, B, K = map(int, input().split())
q = str(max(A-K, 0))
if A+B <= K:
    print("0 0")
else:
    if A >= K:
        w = B
    else:
        w = str(B-K+A)
    print(q, w)
