name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
answer = []
photo_dic = {}

for i in range(len(name)):
    photo_dic[name[i]] = yearning[i]
print(photo_dic)

for i in range(len(photo)):
    for j in range(len(photo[i])):
        # print(photo[i][j])
        photo[i][j] = photo[i][j].replace(photo[i][j], str(photo_dic.get(photo[i][j])))
for i in range(len(photo)):
    for j in range(len(photo[i])):
        if photo[i][j] == 'None':
            photo[i][j] = 0
        else:
            photo[i][j] = int(photo[i][j])
print(photo)

for i in range(len(photo)):
    answer.append(sum(photo[i]))  
print(answer)