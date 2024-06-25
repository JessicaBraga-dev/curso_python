numLista = []
par = []
impar = []
while True:
    numLista.append(int(input(' Digite um número: ')))
    res = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if res in 'N':
        break
for i, v in enumerate(numLista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-='*40)
print(f'A lista completa é {numLista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')