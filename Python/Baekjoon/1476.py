import sys

e_, s_, m_, cnt = 1,1,1,1
e, s, m = map(int, input().split())

while True:
    if e_ == e and s_ == s and m_ == m:
        break
    e_ += 1
    s_ += 1
    m_ += 1
    cnt += 1

    if e_ >= 16:
        e_ -= 15
    if s_ >= 29:
        s_ -= 28
    if m_ >= 20:
        m_ -= 19
    
print(cnt)