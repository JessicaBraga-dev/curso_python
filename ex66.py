from random import randint
print('=-'*35)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*35)
v = 0
while True:
    jogador = int(input('DIGITE UM VALOR: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print('-'*35)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}', end='')
    print(' DEU PAR ' if total % 2 == 0 else ' DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCÊ VENCEU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente ...')
print(f'GAMER OVER! Você venceu {v} vezes.')
