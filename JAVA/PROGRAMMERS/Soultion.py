n = 10
answer = 0
trash = 0
if(n % 2 == 0):
    #짝수
    for i in range(1,n+1):
        if(i % 2 == 0):
            answer += i**2
        else:
            trash += i
else:
    #홀수
    for i in range(1,n+1):
        if(i % 2 == 1):
            answer += i
        else:
            trash += i
print(answer)