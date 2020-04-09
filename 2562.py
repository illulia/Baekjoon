a = 0
c = []
for i in range(1,10):
    b = int(input())
    c.append(b)
    if b > a:
        a = b
print(a)
for i in range(10):
    if a == c[i]:
        print(i)