chicken = 1999 # 정답 222
remain_coupon = 0
answer = 0
while chicken >= 10:
    free_chicken = chicken // 10
    answer += free_chicken
    remain_coupon += chicken % 10
    chicken = free_chicken
    print(chicken, free_chicken, remain_coupon)
while (chicken := remain_coupon + chicken) >= 10:
    remain_coupon = 0
    while chicken >= 10: 
        free_chicken = chicken // 10
        answer += free_chicken
        remain_coupon += chicken % 10
        chicken = free_chicken
    print(chicken, free_chicken, remain_coupon)
    print(answer)