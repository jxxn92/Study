import sys
from itertools import combinations
input = sys.stdin.readline

def is_odd(num):
    if num % 2 == 1:
        return True
    else:
        return False
def is_prime_num(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


while True:
    a = int(input())
    if a == 0:
        break
    
    # if(is_odd(a) and is_prime_num(a)):
