f = str(input('DIGITE UMA FRASE: ')).strip().upper()
p = f.split()
j = ''.join(p)
i = ''
for l in range(len(j) -1, -1, -1):
    i += j[l]
if i == j:
    print('O inverso de {} é {}'.format(j, i))
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palídromo!')
