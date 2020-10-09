a = input()
b = []
c = ""
for i in range(len(a)):
    b.append(a[i])
b.sort()
b.reverse()
for j in b:
    c += j
print(c)