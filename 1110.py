a = int(input())
cheak = a
b = 0
temp = 0
aount = 0
while True:
    temp = a//10 + a%10
    b = (a%10)*10 + temp%10
    aount += 1
    a = b
    if b == cheak:
        break
print(aount)
