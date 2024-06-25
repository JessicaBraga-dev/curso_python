dados = [] #temp
galera = [] #princ
maiorpeso = menorpeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(galera) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    galera.append(dados[:])
    dados.clear()
    res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if res in 'N':
        break
print('-'*30)
print(f'Ao todo você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {maiorpeso}Kg.', end='')
for p in galera:
    if p[1] == maiorpeso:
        print(f' Peso de {p[0]}', end='')
print(f'\nO menor peso foi de {menorpeso}Kg.', end='')
for p in galera:
    if p[1] == menorpeso:
        print(f' Peso foi {p[0]}', end='')
