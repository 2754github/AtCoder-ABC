N = int(input())
S = list(input())

if S[:int(N/2)] == S[int(N/2):]:
    print("Yes")
else:
    print("No")
