sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

for i in sizes:
    tmp = 0
    if i[0] >= i[1]:
        pass
    else:
        tmp = i[0]
        i[0] = i[1]
        i[1] = tmp
# [[60, 50], [70, 30], [60, 30], [80, 40]]

max_width = sizes[0][0]
for i in sizes:
    if i[0] >= max_width:
        max_width = i[0]
    if i[1] >= max_height:
        max_height = i[1]
print(max_width * max_height)