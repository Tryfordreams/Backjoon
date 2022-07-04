A, B = map(int,input().split())
C = int(input())
time = A * 60 + B
total_time = time + C
if total_time < 1440:
    print(total_time//60, total_time%60)
else:
    total_time = total_time - 1440
    print(total_time//60, total_time%60)