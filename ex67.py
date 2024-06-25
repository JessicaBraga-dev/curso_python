tot18 = totm = totf = 0

while True:
    print('-'*35)
    print('CADASTRE UMA PESSOA')
    print('-' * 35)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 35)
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totm += 1
    if sexo == 'F' and idade < 20:
        totf += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos {tot18}')
print(f'Ao todo temos {totm} homens cadastrados')
print(f'E temos {totf} mulheres com menos de 20 anos')