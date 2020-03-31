N = int(input())
S = input()
cnt = 0
for i in range(N-2):
    s = S[i:i+3]
    if s == "ABC":
        cnt += 1
print(cnt)
