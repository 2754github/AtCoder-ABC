N = int(input())
S = []
for _ in range(N):
    S.append(input())
print(len(list(set(S))))
