from datetime import date

nasc = int(input('ANO DE NASCIMENTO: '))
ano = date.today().year
idade = ano - nasc

print('O Atleta tem {}'.format(idade))

if idade <= 9:
    print('CLASSIFICAÇÃO: MIRIM')

elif idade <= 14:
    print('CLASSIFICAÇÃO: INFANTIL')

elif idade <= 19:
    print('CLASSIFICAÇÃO: JÚNIOR')

elif idade <= 25:
    print('CLASSIFICAÇÃO: SÊNIOR')

else:
    print('CLASSIFICAÇÃO: MASTER')