import sys

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
    
    def size(self):
        stack_size = len(self.stack)
        
        return stack_size




s = stack()
num = int(sys.stdin.readline())

for _ in range(num):    

    input = sys.stdin.readline().split()
    order = input[0]

    if order == 'push':
        value = input[1]
        s.push(value)
    elif order == 'top':
        print(s.peek())
    elif order == 'size':
        print(s.size())
    elif order == 'pop':
        print(s.pop())
    elif order == 'empty':
        print(int(s.isEmpty()))
    




