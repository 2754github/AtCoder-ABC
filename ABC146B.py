N = int(input())
S = list(input())

ans = ''
for i in range(len(S)):
    a = ord(S[i])+N
    if a > 90:
        a = a-26
    ans += chr(a)
print(ans)
