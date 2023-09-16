n,d = map(int,input().split())   # 입력
lst = [i for i in range(1,n+1)]
ans = ''
cnt = 0
for i in range(n-1):
    cnt = (cnt + d-1)%len(lst)   # 꺼내야 할 원소의 위치 찾기
    ans += str(lst.pop(cnt))
ans += str(lst[0])
