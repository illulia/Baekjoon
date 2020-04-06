a = int(input())
b = [0,1]
for i in range(a):
    c = b[i] + b[i+1]
    b.append(c)
print(b[10])