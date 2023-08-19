a = [1,2,3,4]; b = [-3,-1,0,2]
answer = []
for i in range(len(a)):
    s = a[i] * b[i]
    answer.append(s)

print(sum(answer))

# return sum([x*y for x, y in zip(a,b)])

#^ zip을 사용하여 두 리스트에서 값을 하나씩 묶어서 저렇게도 사용할 수 있다.