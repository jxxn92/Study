# 문제 해결을 고민 하던 중 부분함수 subset을 사용하면 간단하게 풀 수 있어서 사용함.
spell = ["p", "o", "s"]
dic = ["sod", "eocd", "qixm", "adio", "soo"]

spell = set(spell)

for i in dic:
    if spell.issubset(set(i)):
        print(1)