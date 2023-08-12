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
    
    def show(self):
        s = []
        for i in range(self.list()):
            s.append(i)
        
        return s
    
    def size(self):
        stack_size = len(self.list())
        return stack_size
    
s = stack()
answer = []
str1 = input("문자열을 입력하시오: ")
str1 = str1.lower()

for x in str1:
    if x.isalpha():
        answer.append(x)

str2 = list(reversed(answer))
str2 = ''.join(str2)
answer = ''.join(answer)

print(answer, str2)
# str2 =list(''.join(reversed(answer)))
# str2 = ''.join(str2)
# str3 = ''.join(answer)
# print(str3, str2)
if answer == str2:
    print("회문")
else:
    print("회문 아님")