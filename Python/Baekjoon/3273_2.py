# baekjoon 3273 두 수의 합
# 단순하게 두 수 뽑아서 target 값과 같으면 개수를 세는 방식으로 하려 했지만 이 방법은 경우 의 수가 너무 많아서 메모리와 시간 초과가 발생한다
# 이런 경우에는 투 포인터 알고리즘이라는게 존재하는데 말그대로 두개의 가리키는 지점을 생성하여 
# 배열을 정렬한 다음 맨 앞 과 맨 뒤를 가리키는 포인터를 만들고 그 두개를 적절히 움직여 값을 생성시키는 것이다.

import sys
input = sys.stdin.readline

data = []
n = int(input())
data = list(map(int, input().split()))
target = int(input())
data.sort()
cnt = 0
fp = 0
ep = len(data) - 1  

while fp != ep:
    if data[fp] + data[ep] == target:
        ep -= 1
        cnt += 1
    else:
        if data[fp] + data[ep] > target:
            ep -= 1
        else:
            fp += 1
print(cnt)