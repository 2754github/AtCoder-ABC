import sys
N, M = map(int, input().split())
A = ["*"]*N
for _ in range(M):
    s, c = map(int, input().split())
    if A[s - 1] == "*":
        A[s - 1] = str(c)
    else:
        if A[s - 1] == str(c):
            pass
        else:
            print(-1)
            sys.exit()

A_replace = [a.replace("*", "0") for a in A]
if N == 1:
    print(A_replace[0])
elif N == 2:
    if A_replace[0] == "0":
        print(-1)
    else:
        print("".join(A_replace))
elif N == 3:
    if A_replace[0] == "0":
        print(-1)
    else:
        print("".join(A_replace))
