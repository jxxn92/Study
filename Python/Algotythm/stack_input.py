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
        
        return self.stack[-1]
    
s = stack()

num = input("정수 배열의 크기: ")

for _ in range(int(num)):
    k = input()
    s.push(k)
for _ in range(int(num)):
    print(s.pop(), end= " ")

    
