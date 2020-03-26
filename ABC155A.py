A, B, C = map(int, input().split())
print("Yes" if len(list(set([A, B, C]))) == 2 else "No")
