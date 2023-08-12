import sys
# 생성자 push pop isempty peek size 
class stack():
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        is_empry = 0
        if len(self.stack) == 0:
            is_empry = 1
        return is_empry

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        pop_object = -1
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
        return len(self.stack)

s = stack()

n = int(input())
lst = []

for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == '1':
        s.push(a[1])
    elif a[0] == '2':
        print(s.pop())
    elif a[0] == '3':
        print(s.size())
    elif a[0] == '4':
        print(s.isEmpty())
    elif a[0] == '5':
        print(s.peek())
    