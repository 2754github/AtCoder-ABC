S = input()
Q = int(input())
for _ in range(Q):
    s = input().split()
    if len(s) == 1:
        S = S[::-1]
    else:
        if s[1] == "1":
            S = s[2] + S
        else:
            S = S + s[2]
print("".join(S))
