lst = []
lst2 = []
def self_number(num):
    if num < 10:
        return num*2
    # elif num < 100:
    else:
        s = str(num)
        sum_num = 0
        for i in range(len(s)):
            sum_num += int(s[i])
        
        return num+sum_num

for i in range(1,10000):
    lst.append(self_number(i))
    lst.sort()

for i in range(1,10000):
    if i not in lst:
        print(i)