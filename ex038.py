n1 = float(input('DIGITE A PRIMEIRA NOTA: '))
n2 = float(input('DIGITE A SEGUNDA NOTA: '))
media = (n1 + n2)/2
print('TIRANDO {} E {}, A MÉDIA DO ALUNO É {}'.format(n1,n2,media))
if media >= 7.0:
    print('O aluno está APROVADO.')
elif media >= 5.0:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está REPROVADO.')


''' MANEIRAS DE FAZER
if media >= 5.0 and média < 7:
    print('O aluno está em RECUPERAÇÃO.')
--------------------------------------------
if 7 > media >= 5.0 :
    print('O aluno está em RECUPERAÇÃO.')
'''