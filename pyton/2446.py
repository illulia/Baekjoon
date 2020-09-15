a = int(input())
b = 1
c = a-2
for i in range(a*2-1):
    if a != 0:
        print(' '*i+'*'*(a*2-1))
        a -= 1 
    else:
        print(' '*c+'*'*(b*2+1))
        b += 1
        c -= 1