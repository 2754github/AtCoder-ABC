import math
a, b, x = map(int, input().split())

if x > (a**2)*b/2:
    theta = math.atan((2*(a**2)*b-2*x)/(a**3))*180/math.pi
else:
    theta = math.atan((a*b**2)/(2*x))*180/math.pi

print(theta)
