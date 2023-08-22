nums = [1,2,3,4] 
nums.sort()
lst = [(nums[i]+nums[j]+nums[k]) for i in range(len(nums)) for j in range(i+1, len(nums)) for k in range(j+1, len(nums))]
lst2 = []
cnt = 0
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False  
    return True

for i in lst:
    if isPrime(i):
        cnt += 1
    else:
        pass
print(cnt)
