a = 5; b = 24
#윤년 1년 366일

# a월 b일이 기준일인 2016년 1월 1일 금요일부터 며칠이 지났는지 구하고,
# 그걸 7로 나눈 나머지로 무슨 요일인지 알 수 있다.

# 2016년 5월 24일 
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
# 5월 24일 같은 경우는 1~4월 까지의 날짜 다 더하고 24일 까지 더한 다음에 7로 나눈 나머지를 비교하면 요일을 알 수 있다.
s = 0
for i in range(1,a):
    s += month[i-1]
s += b-1
day = s % 7

if day == 0:
    print("FRI")
elif day == 1:
    print("SAT")
elif day == 2:
    print("SUN")
elif day == 3:
    print("MON")
elif day == 4:
    print("TUE")
elif day == 5:
    print("WED")
elif day == 6:
    print("THU")