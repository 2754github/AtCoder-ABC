S = input()
a = int(S == S[::-1])
N = len(S)
S1 = S[:(N-1)//2]
b = int(S1 == S1[::-1])
S2 = S[(N+3)//2-1:]
c = int(S2 == S2[::-1])

print("Yes" if a*b*c == 1 else "No")
