valores = []
maior = 0
menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print('-=' * 40)
print(f'Você digitou os valores {valores}')
print(f'O MAIOR valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO MENOR valor digitado foi {menor} nas posiçoes ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
