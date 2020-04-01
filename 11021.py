import sys
x = int(sys.stdin.readline())
for i in range(1,x+1):
    A,B = map(int,sys.stdin.readline().split())
    print("Case #"+str(i)+": "+str(A+B)) 
