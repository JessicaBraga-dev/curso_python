cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', ' vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o num {cont[num]}')
    else:
        print('Tente novamente. ', end='')
        continue
    while True:
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if res in 'SN':
            break
    if res == 'N':
        break

