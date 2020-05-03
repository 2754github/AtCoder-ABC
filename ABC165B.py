X = int(input())
Y = 100
cnt = 0
while True:
    if Y >= X:
        print(cnt)
        break
    cnt += 1
    Y = Y+int(Y*0.01)
