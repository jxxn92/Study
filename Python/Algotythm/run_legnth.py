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
str1 = input("문자열을 입력하시오: ")
str1 = str1.lower()
str2 = list(set(str1))
answer = []
cnt = 0
dic = {}
for i in str2:
    for j in str1:
        if i == j:
            cnt += 1
    answer.append(cnt)
    dic[i] = cnt
    cnt = 0

for value,key in dic.items():
    print(key,value, end= "", sep ='')


# str1 = input("문자열을 입력하시오: ")
# str1 = str1.lower()
# str2 = set(str1)
# str3 = list(str2)
# count = 0
# arr = []
# for i in str2:
#     for j in str1:
#         if j == i:
#             count = count + 1
#     arr.append(count)
#     count = 0
# print(str3[0],arr[0],"",str3[1],arr[1])