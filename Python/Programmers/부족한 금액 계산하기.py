price = 3 
money = 20
count = 4
s = 0

for i in range(count):
    s = s + price*(i+1)
    
if money - s >= 0:
    print(0)
else:
    print(s-money)