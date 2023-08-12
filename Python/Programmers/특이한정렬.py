numlist = [10000,20,36,47,40,6,10,7000]	
n = 30
negative = []
negative2 = []
answer = []
# 음수만 따로 출력해서 리스트에 저장
for i in numlist:
    if i-n < 0:
        negative.append(i-n)
print(negative)

# negative 리스트 복사
for i in negative:
    negative2.append(i)

# numlist에서 n을 뺀 값을 리스트에 저장
difference = [i - n for i in numlist]
print(difference)

# 절댓값으로 바꾸기는 하는데 음수쪽 - 때기 위해서 설정
distance = [num-n if num-n >= 0 else n-num for num in numlist]
distance.sort()
# print(distance)

#distance 리스트에서 i번째와 i+1번째 비교해서 두 값이 같으면 i+1을 음수로 변경
for i in range(len(distance)-1):
    if distance[i] == distance[i+1]:
        distance[i+1] = -distance[i+1]
# print(distance)
# 위에 비교하는 식으로는 모든 음수를 비교 할 수 없어서 음수가 존재한다면 복사한
# negative2에서 값을 제거하면서 음수로 변경하지 않은 값들만 놔둠
for i in negative:
    if i in distance:
        key = negative.index(i)
        #print(key)
        negative2.remove(negative[key])
# print(difference)
# print(negative, negative2)
# print(distance)

# 남은 값들을 인덱스 값으로 찾아서 음수로 변경
for i in range(len(negative2)):
    if abs(negative2[i]) in distance:
        distance[distance.index(abs(negative2[i]))] = negative2[i]
# print(distance)

for i in distance:
    answer.append(i+n)
print(answer)