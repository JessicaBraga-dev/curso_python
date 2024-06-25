print('-'*35)
print('{:^35}'.format('LOJA SUPER BARATO'))
print('-'*35)
tot = totmil = menor = cont = 0
barato = ' '
while True:
    n = str(input('Nome do Produto: '))
    p = float(input('Preço: R$ '))
    cont += 1
    tot += p
    if p > 1000:
        totmil += 1
    if cont == 1 or p < menor:
        menor = p
        barato = n

    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break
print(f'O total da compra foi {tot:.2f}')
print(f'Temos {totmil} custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
