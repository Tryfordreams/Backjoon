T = int(input())
for i in range(T):
    ans = input()
    ans_list = [0] * len(ans)

    for i in range(len(ans)):
        if i == 0:
            if ans[i] == "O":ans_list[i] = 1
            else: ans_list[i] = 0
        else:
            if ans[i] == "O":
                ans_list[i] = ans_list[i-1] + 1
            else : ans_list[i] == 0
    sum = 0
    for i in ans_list:
        sum += i
    print(sum)