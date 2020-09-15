from sys import stdin
a,b,c = map(int,stdin.readline().split())
d = 0
if b < c:
    d = a//(c-b)
    print(d+1)
else:
    print(-1)
