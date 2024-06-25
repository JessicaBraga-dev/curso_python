from datetime import date

nasc = int(input('ANO DE NASCIMENTO: '))
ano = date.today().year
idade = ano - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,ano))

if idade < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
    print('Seu alistamento será em {}'.format(ano + (18 - idade)))
elif idade == 18:
    print('Você tem que se alista IMEDIATAMENTE')
else:
    print('Você já deveria ter se alistado há {} anos'.format((ano - nasc)-18))
    print('Seu alistamento foi em {}.'.format(nasc + 18))