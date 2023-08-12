class stack():
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        is_empty = False
        
        if len(self.stack) == 0:
            is_empty = True
        
        return is_empty
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        pop_object = None
        if self.isEmpty():
            pass
        else:
            pop_object = self.stack.pop()
        
        return pop_object
    
    def peek(self):
        peek_object = None
        if self.isEmpty():
            pass
        else:
            peek_object = self.stack[-1]
        
        return peek_object
    
    def clear(self):
        self.stack.clear()

s = stack()
n = input()

for _ in range(int(n)):
    line = input()

    for i in line:
        if i == '(':
            s.push(i)
        elif i == ')':
            if s.isEmpty is True:
                s.push(i)
                break
            else:
                if s.peek() == '(':
                    s.pop()
                else:
                    s.push(i)
    
    if s.isEmpty() is True:
        print('YES')
    else:
        print('NO')
    s.clear()
