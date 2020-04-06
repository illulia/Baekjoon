num = []
for i in range (7):
    a = int(input())
    if a%2 == 1:
        num.append(a)
    else:
        pass
if sum(num) != 0:
    num.sort()
    print(sum(num))
    print(num[0])
else:
    print("-1")
