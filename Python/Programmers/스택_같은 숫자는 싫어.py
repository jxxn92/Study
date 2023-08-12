class stack():
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        
        return is_empty
    
    def push(self, item):
        self.stack.append(item)
    
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
    
    def sise(self):
        return len(self.stack)    

array = [1, 3, 3, 0, 1, 1]
s = stack()

for x in array:
    if s.isEmpty():
        s.push(x)
    else:
        if x == s.peek():
            pass
        else:
            s.push(x)
print(s.stack)
