ans_list = []
for i in range(10):
    ans_list.append(int(input())%42)
ans_set = set(ans_list)
print(len(ans_set))