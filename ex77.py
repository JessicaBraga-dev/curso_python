lista = []
while True:
    n = (int(input('Digite um valor: ')))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor duplicado. Não vou adicionar ...')
    res = str(input('Quer continuar: [S/N]')).strip().upper()[0]
    if res in 'N':
        break
print('-='*40)
lista.sort()
print(f'Você digitou os valores {lista}')


