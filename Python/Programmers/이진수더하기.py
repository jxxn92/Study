bin1 = "10"
bin2 = "11"
bin1 = bin1[::-1]
bin2 = bin2[::-1]

ans_bin1 = 0
ans_bin2 = 0

for i in range(len(bin1)):
    if i == 0:
        x = 1 if bin1[i] == '1' else 0
        ans_bin1 += x
    else:
        if bin1[i] == '1':
            ans_bin1 = ans_bin1 + ( 2**i)

for i in range(len(bin2)):
    if i == 0:
        x = 1 if bin2[i] == '1' else 0
        ans_bin2 += x
    else:
        if bin2[i] == '1':
            ans_bin2 = ans_bin2 + ( 2**i)
ans_sum = ans_bin1 + ans_bin2

print(bin(ans_sum)[2:])