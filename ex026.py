from random import randint
c = randint(0,5)
print('-=-'*50)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar......')
print('-=-'*50)
n = int(input('Em que número pensei? '))
print('PROCESSANDO...')
if n == c:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(c,n))