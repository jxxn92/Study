while True:
    stack = []
    expression = input()

    if expression == '.':
        break
    

    for exp in expression:
        if exp == '(' or exp == '[':
            stack.append(exp)
        elif exp == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(exp)
                break
        elif exp == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(exp)
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")
