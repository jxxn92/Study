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
    
s = stack()
k = stack()

num1 = int(sys.stdin.readline())
str1 = set(map(int, sys.stdin.readline().split()))

num2 = int(sys.stdin.readline())
str2 = list(map(int, sys.stdin.readline().split()))

for x in str2:
    if x in str1:
        print(1)
    else:
        print(0)