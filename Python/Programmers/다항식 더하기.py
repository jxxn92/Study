
polynomial = "3x + 7 + x"
coef = 0
const = 0
for term in polynomial.split(' + '):
    if 'x' in term:
        if len(term) != 1:
            coef += int(term[:-1]) - 1
        coef += 1 
    else:
        const += int(term)
answer = []
if coef != 0:
    answer.append('x' if coef == 1 else f'{coef}x')
if const != 0:
    answer.append(str(const))
print ' + '.join(answer) if answer else '0'