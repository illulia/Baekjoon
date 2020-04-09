import sys
a = int(sys.stdin.readline())
b = [0] * 10001
for i in range(a):    
    b[int(sys.stdin.readline())] +=1

for i in range(10001):
    sys.stdout.write('%s\n' % i * b[i])
