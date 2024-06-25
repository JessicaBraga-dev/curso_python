velho = 0
nomeh = ''
soma = 0
media = 0
totm = 0
for pess in range(1, 5):
    print('----- {}º Pessoa -----'.format(pess))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma += idade
    if pess == 1 and sexo in 'Mm':
        velho = idade
        nomeh = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomeh = nome
    if sexo in 'Ff' and idade < 20:
        totm += 1
media = soma / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(velho,nomeh))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totm))













