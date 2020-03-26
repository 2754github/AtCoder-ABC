N = int(input())
A = list(map(int, input().split()))
flg = 0
for a in A:
    if a % 2 == 0:
        if not(a % 3 == 0 or a % 5 == 0):
            flg += 1

print("APPROVED" if flg == 0 else "DENIED")
