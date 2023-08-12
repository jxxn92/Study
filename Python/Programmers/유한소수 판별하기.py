a = 1
b = 16
lst1 = []
lst2 = []
x = a/b

if a  > b:
    if x.is_integer():
        print(1)
    else:
        print(2)
else:
    for i in range(2,a+1):
        if a % i == 0:
            lst1.append(i)
    for i in range(2,b+1):
        if b % i == 0:
            lst2.append(i)
    comb = list(set(lst1) & set(lst2))
    if len(comb)==0:
        pass
    else:
        comb_num = comb[-1] 
        a = int(a/comb_num) ; b = int(b/comb_num)
    answer = []
    for i in range(2, b+1):
        if b % i == 0:
            answer.append(str(i))
    if len(answer) == 1:
        if answer[0] == '2' or answer[0] == '5':
            print(1) 
        else:
            print(2)
    else:
        if ('2' in answer and '5' in answer):
            print(1)
        else:
            print(2)

이거 수정 할 때 위에 최대공약수 구하는거 함수로 빼던가 최대공약수 알고리즘 파이썬에 함수로 존재하면 그거 써서 보기 쉽게 만들것