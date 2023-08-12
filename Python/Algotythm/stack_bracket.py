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
        peek_object = -1
        if self.isEmpty():
            pass
        else:
            peek_object = self.stack[-1]
        
        return peek_object
s = stack()
count = 0

brack = input("수식: ")

for x in brack:
    if x == '(':
        count += 1
        s.push(count)
    elif x == ')':
        if s.peek() == count:
            s.push(count)
        elif x == ')':
            count -= 1
            s.push(count)
    
    print(s.stack)
