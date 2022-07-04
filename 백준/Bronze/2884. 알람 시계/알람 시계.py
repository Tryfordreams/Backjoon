H, M = map(int,input().split())
if M >= 45: print(H,M-45)
else:
    if H != 0:
        H = H - 1
        M = 60 + (M-45)
        print(H,M)
    else:
        M = 60 + (M-45)
        print(23,M)