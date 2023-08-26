a = 5
b = 3
n = 21

answer = 0
    # 내가 마지막에 총 먹은 콜라의 개수

while True:
    extra = 0
    answer += b*(n // a) # 내가 다시 받을 수 있는 콜라의 병 수
    extra = n % a  # 콜라를 a병이상 가져가야 1병을 받을 수 있기 때문에 a병 미만일 경우 남은 병의 수를 저장
    n = (b*(n//a)) + (extra) # 이제 절반으로 줄 었으니까 다시 마트가서 받을 수 있는 병의 수 + 혹시나 남은 병의 수 

    if n < a:
        break
print(answer)