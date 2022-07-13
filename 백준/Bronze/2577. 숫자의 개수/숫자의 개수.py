A = int(input())
B = int(input())
C = int(input())
d = A * B * C
D = str(d)
for i in range(10):
    num = 0
    for j in D:
        if int(j) == i: num += 1
    print(num)