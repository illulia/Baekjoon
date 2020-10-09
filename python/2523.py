a = int(input())
b = 1
for i in range(1,2*a):
    if b != a:
        print('*'*i)
        b += 1 
    elif b == a:
        print('*'*a)
        a -= 1
        b -= 1