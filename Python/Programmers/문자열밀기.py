# A 와 B 를 비교 하느데 같으면 0 같지 않으면 밀어야 하는 최소 이동횟수를 리턴하는 문제.
A = "atat"
B = "tata"
A = list(A)
B = list(B)
cnt = 0
# 
answer = []
if A == B:
    print(0)
else:
    # 오른쪽으로 밀 경우 , 왼쪽으로 밀 경우 두개를 구해서 최소 값을 리턴 해야한다.
    # for i in range(len(copy1)):
    #     # 왼쪽으로 미는 경우(맨 앞의 값이 맨 뒤로 오는 경우)
    #     tmp = copy1[0] # 맨 앞의 값을 임시 변수에 저장
    #     # print(tmp)
    #     copy1.remove(tmp) # 어짜피 앞에서 부터 값이 삭제되니 remove로 앞에 있던 문자 부터 삭제
    #     copy1.append(tmp) # 리스트에서 맨 뒤에 값 추가 append 사용
    #     cnt += 1 # 횟수 측정을 위해서 cnt++
    #     # print(A)
    #     if copy1 == B:
    #         answer.append(cnt)
    #         break
    #     else:
    #         continue
    for i in range(len(A)):
        # 오른쪽으로 미는 경우(맨 뒤의 값이 맨 앞으로 오는 경우)
        tmp2 = A[-1]
        del A[-1]
        A.insert(0,tmp2)
        cnt += 1
        if A == B:
            answer.append(cnt)

if len(answer) == 0:
    print(-1)
else:
    print(min(answer))

        
