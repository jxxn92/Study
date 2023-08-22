num_list = [12, 4, 15, 46, 38, -2, 15]
negative = []
for i in num_list:
    if i < 0:
        print(num_list.index(i)+1)
        negative.append(i)
if len(negative) == 0:
    print(-1)
else:
    num_list.index(negative[0])