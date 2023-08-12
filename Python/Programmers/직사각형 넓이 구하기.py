dots = [[-1, -1], [1, 1], [1, -1], [-1, 1]]	# lst = [dots[i] for i in range(len(dots))]
for i in range(len(dots)):
    if i == 0:
        p1 = dots[i]
    elif i == 1:
        p2 = dots[i]
    elif i == 2:
        p3 = dots[i]
    elif i == 3:
        p4 = dots[i]

length = max(p1[0],p2[0],p3[0],p4[0]) - min(p1[0],p2[0],p3[0],p4[0])
height = max(p1[1],p2[1],p3[1],p4[1]) - min(p1[1],p2[1],p3[1],p4[1])
print(length * height)
