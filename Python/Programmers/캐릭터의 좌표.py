keyinput =  ["left", "right", "up", "right", "right"]
board = [11, 11]
now = [0, 0]
box = board[0] // 2
boy = board[1] // 2

print(box, boy)

for x in keyinput:
    if (now[1] < boy):
        if x == 'up':
            now[1] += 1
    if (now[1] > -boy):
        if x == 'down':
            now[1] -= 1
    if (now[0] < box):
        if x == 'right':
            now[0] += 1
    if (now[0] > -box):
        if x == 'left':
            now[0] -= 1
    print(now)