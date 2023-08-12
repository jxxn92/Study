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
    
    def list(self):
        stack_list = list(self.stack)
        return stack_list
    
    def size(self):
        stack_size = len(self.list())
        return stack_size

    def stack_sum(self):
        sumOfStack = 0
        for i in range(self.size()):
            sumOfStack += int(self.stack[i])
        
        return int(sumOfStack)

    
s = stack()
command = input()

for _ in range(int(command)):
    num = input()
    if int(num) != 0:
        s.push(num)
    else:
        s.pop()

print(s.stack_sum())