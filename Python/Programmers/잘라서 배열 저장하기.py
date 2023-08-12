import math
my_str = "abc1Addfggg4556b"
n = 6

lst = [my_str[i*n:i*n+n] for i in range(math.ceil(len(my_str)/n))]
print(lst)