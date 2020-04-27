A, B, C, D = map(int, input().split())
Ta = -(-C//B)
Ao = -(-A//D)
print('Yes' if Ta <= Ao else 'No')
