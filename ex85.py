matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maior = somacol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {[l], [c]}: '))
print('-=' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('-=' * 40)
print(f'A soma dos valores pares é {somapar}')
for l in range(0, 3):
    somacol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {somacol}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')