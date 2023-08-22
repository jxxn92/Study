num_list = [3, 4, 5, 2, 1]
sum_num = 0
mul_num = 1
for i in num_list:
    sum_num += i
for j in num_list:
    mul_num *= j

if mul_num < sum_num**2:
    print(1)
else:
    print(0)