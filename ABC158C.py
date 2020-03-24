import sys
A, B = map(int, input().split())
for x in range(1, 1300):
    if int(0.08 * x) == A and int(0.1 * x) == B:
        print(x)
        sys.exit()
print(-1)
