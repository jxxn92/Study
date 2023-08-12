# 숫자를 isalpha로 뽑으려고 했으나 이렇게 뽑으면 몇의 자리 수인지 알 수 없기 때문에 사람들의 이야기를 봤는데 정규식을 사용하면 간단하게 뽑을 수 있다고 나와있어서 사용한다.
# 정규식을 사용하는 방법도 알고는 있어야 할 것 같다.
import re

my_string = "aAb1B2cC34oOp"

lst = re.findall('\d+', my_string)
sum_num = 0
for i in lst:
    sum_num += int(i)
print(sum_num)
