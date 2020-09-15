a = int(input())
for i in range(a):
    num = 0
    b = list(map(int,input().split()))
    c = sum(b[1:]) / b[0]
    for j in range(1,len(b)):
        if b[j] > c:
            num += 1
    print(str('%.3f' % round(num/b[0]*100, 3))+'%')
            