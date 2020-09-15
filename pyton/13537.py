from sys import stdin
a = int(stdin.readline())
b = list(map(int,stdin.readline().split()))
c = int(stdin.readline())
for i in range(c):
    x = 0
    d,e,f = map(int,stdin.readline().split())
    for j in range(d-1,e):
        if b[j] > f:
            x += 1
        else:
            pass
    print(x)
