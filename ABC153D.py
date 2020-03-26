H = int(input())
cnt = 0
ans = 1
while H != 1:
    H = H//2
    cnt += 1
    ans += 2**cnt
print(ans)
