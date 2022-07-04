N = int(input())
score = list(input().split())
int_score = []
for i in score:
    int_score.append(int(i))
max_number = max(int_score)
lie_score = []
for i in int_score:
    lie_score.append(i / max_number * 100)
sum = 0
for i in lie_score:
    sum += i
print(sum/N)