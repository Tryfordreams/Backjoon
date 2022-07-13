N = input().upper()
N_list = [0] * 26
for i in N:
    N_list[ord(i)-65] += 1
sorted_list = sorted(N_list)
if sorted_list[-1] == sorted_list[-2] : print("?")
else:
    a = chr(N_list.index(max(N_list))+65)
    print(a.upper())