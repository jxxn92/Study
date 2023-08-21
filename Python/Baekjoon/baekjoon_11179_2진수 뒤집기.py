value = int(input())
ten = '0b'
b = bin(value)[2:]
b = b[::-1]
ans = ten+b

a = int(ans, 2)
print(a)
