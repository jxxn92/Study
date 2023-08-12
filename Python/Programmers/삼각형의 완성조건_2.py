sides = [3, 6]

max_line = max(sides)
min_line = min(sides)
sum_line = 0
answer = []
for i in sides:
    sum_line += i 

for i in range(1,max_line+1): # 제일 긴 변이 11인 경우
    if min_line+i > max_line:
        answer.append(i)
for i in range(max_line+1,sum_line):
    answer.append(i)
print(len(answer))