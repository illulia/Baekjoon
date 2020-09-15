a = int(input())
b = list(map(int,input().split()))
b.sort()
for i in range(a):
    b[i] = b[i]/b[a-1]*100
print(sum(b)/a)