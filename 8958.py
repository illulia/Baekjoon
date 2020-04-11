a = int(input())
for i in range(a):
    b = input()
    c = 0
    d = 0
    for i in range(len(b)):
        if b[i] == 'O':
            c += 1
            d +=c
        elif b[i] == 'X':
            c = 0
    print(d)
