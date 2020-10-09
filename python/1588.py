a = list(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(d):
    for j in range(len(a)):
        if a[j] == "1":
            a.insert(j+1,'3')
            a.insert(j+2,'2')
            print(a)
        elif a[j] == "2":
            a.insert(j+1,'1')
            a.insert(j+2,'1')
        elif a[j] == "3":
            a.insert(j-1,'2')
            a.insert(j+1,'3')