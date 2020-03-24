A11, A12, A13 = map(int, input().split())
A21, A22, A23 = map(int, input().split())
A31, A32, A33 = map(int, input().split())
A = [A11, A12, A13, A21, A22, A23, A31, A32, A33]
N = int(input())
for _ in range(N):
    b = int(input())
    if b in A:
        A[A.index(b)] = 0

if A[0] == 0 and A[1] == 0 and A[2] == 0:
    print("Yes")
elif A[3] == 0 and A[4] == 0 and A[5] == 0:
    print("Yes")
elif A[6] == 0 and A[7] == 0 and A[8] == 0:
    print("Yes")
elif A[0] == 0 and A[3] == 0 and A[6] == 0:
    print("Yes")
elif A[1] == 0 and A[4] == 0 and A[7] == 0:
    print("Yes")
elif A[2] == 0 and A[5] == 0 and A[8] == 0:
    print("Yes")
elif A[0] == 0 and A[4] == 0 and A[8] == 0:
    print("Yes")
elif A[2] == 0 and A[4] == 0 and A[6] == 0:
    print("Yes")
else:
    print("No")
