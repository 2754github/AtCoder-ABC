N = int(input())
f = 0
for i in range(1, 10):
    if (N % i == 0 and N/i < 10):
        f = f+1
if f > 0:
    print("Yes")
else:
    print("No")
