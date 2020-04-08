N = int(input())


def divisors(a):
    divisors = []
    for i in range(1, int(a**0.5)+1):
    if a % i == 0:
    divisors.append(i)
    if i != a//i:
    divisors.append(a//i)
    divisors.sort()  # 昇順
    # divisors.sort(reverse=True) # 降順
    return divisors


d = divisors(N)
l = len(d)
if l % 2 == 0:
    a = d[int(l/2)]+d[int(l/2-1)]
else:
    a = d[int((l-1)/2)]*2
print(a-2)
