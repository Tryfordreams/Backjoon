T = int(input())
for i in range(T):
    R, S = map(str,input().split())
    r = int(R)
    for i in S:
        print(i*r, end = "")
    print("")