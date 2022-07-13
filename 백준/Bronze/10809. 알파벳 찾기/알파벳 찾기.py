alpha = [-1] * 26
S = input()
for i in range(len(S)):
    i_index = ord(S[i])-97
    if alpha[i_index] == -1:
        alpha[i_index] = i

for i in alpha: print(i)