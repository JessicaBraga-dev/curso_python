valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    res = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if res in 'N':
        break
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O valor 5 faz parte da lista! ')
else:
    print(f'O valor 5 não foi encontrado na lista! ')