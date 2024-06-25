from random import randint
c = randint(0,10)
print('Sou seu Computador ... \n'
      'Acabei de pensar em um número entre 0 e 10. \n'
      'Será que você consegue adivinhar qual foi?')
a = False
totp = 0
while not a:
    p = int(input('Qual é seu palpite? '))
    totp += 1
    if p == c:
         a = True
    else:
        if p < c:
            print('Mais... Tente novamente.')
        else:
            print('Menos... Tente novamente.')
print('Acertou com {} tentativas. PARABÉNS'.format(totp))
