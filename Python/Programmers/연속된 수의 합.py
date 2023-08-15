'''
홀수랑 짝수를 나눠서 num 그러니가 리스트의 개수 total 연속된 num개의 숫자의 합을 제공
1) 홀수인 경우
    total을 num으로 바로 나눠서 리스트에다가 num이 3인 경우 n-1 n n+1 을 넣으면 
2) 짝수인 경우
    1부터 num-1 까지의 총 합을 구해서 total 에다가 뺀 다음 num 값으로 나누면 값이 나온다.
    그 값이 첫값 num이 4인 경우 n n+1 n+2 n+3 구한다.
'''
answer = []
num = 5
total = 5
standard = 0
sum_standard = 0
# 기준 값을 구하기 위해서 총합에서 뺄 수를 만들기 위해서 사용
for i in range(1,num):
    sum_standard+=i
# 짝수 일 때 홀수 일 때 구분해서 사용

standard = (total - sum_standard) // num
for i in range(num):
    answer.append(standard+i)
print(answer)