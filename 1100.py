White_list = []
for i in range(4):
    a = input()
    for j in (0,2,4,6):
        White_list.append(a[j])
    b = input()
    for k in (1,3,5,7):
        White_list.append(b[k])
print(White_list.count("F"))