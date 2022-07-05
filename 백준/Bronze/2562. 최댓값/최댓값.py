R_list = []
for i in range(9):
    R_list.append(int(input()))
Maxnumber = max(R_list)
index = R_list.index(Maxnumber)
print(Maxnumber)
print(index+1)