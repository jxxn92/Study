s = "1234"
answer = []
if len(s) >= 4 or len(s) <=6:
    for i in s:
        if i.isnumeric():
            answer.append(1)
        else:
            answer.append(0)
    if sum(answer) == len(s):
        print(True)
    else:
        print(False)
else:
    print(False)

    