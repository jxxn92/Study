quiz = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]	

lst = [quiz[i:i+1] for i in range(len(quiz))]
cal = []
answer = []
for i in range(len(lst)):
    cal.append(str(quiz[i]).split())
    result = cal[0][4]
    op1 = cal[0][0]
    op2 = cal[0][2]
    opsum = int(op1) + int(op2)
    opmin = int(op1) - int(op2)
    oper = cal[0][1]
    if str(oper) == '+':
        if int(opsum) == int(result):
            answer.append("O")
        else:
            answer.append("X")
    elif str(oper) == '-':
        if int(opmin) == int(result):
            answer.append("O")
        else:
            answer.append("X")
    cal.clear()
print(answer)