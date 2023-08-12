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
        return len(s.stack)
    

s = stack()

str1 = input("정수를 입력하시오: ")

for x in str1:
    if x not in s.stack:
        s.push(x)

print(*s.stack, sep='')
print(s.size())