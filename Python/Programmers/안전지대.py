board = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
danger = []
r = len(board)-1
c = len(board)-1
all_count = (r+1) * (c+1)
# print(r,c,all_count)
for i in range(r+1):
    for j in range(c+1):
        if board[i][j] == 1:
            danger.append((i,j)) # 원 점
            danger.append((i,j-1)) # 왼쪽
            danger.append((i,j+1)) # 오른쪽
            danger.append((i-1,j)) # 위쪽
            danger.append((i+1,j)) # 아래쪽
            danger.append((i-1,j-1)) # 왼쪽 위
            danger.append((i-1,j+1)) # 오른쪽 위
            danger.append((i+1,j-1)) # 왼쪽 아래
            danger.append((i+1,j+1)) # 오른쪽 아래
# print(danger)
answer = []
for i in danger:
    if (i[0] >= 0 and i[1] >= 0 and i[0] <= r and i[1] <= c):
        answer.append(i)
my_str = set(answer)
answer = list(my_str)
# print(answer)
print(all_count-len(answer))