import math


def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


X = int(input())
i = 0
while True:
    i += 1
    if is_prime(i) and i >= X:
        print(i)
        break
