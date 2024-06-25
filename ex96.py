from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 25)
    print(f'contando de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.8)
            cont += p
        print(' > FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.8)
            cont -= p
        print(' > FIM!')


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 25)
print('Agora e sua vez de personaizar a contagem')
ini = int(input('Início:    '))
fim = int(input('Fim:       '))
pas = int(input('Passos:    '))
contador(ini, fim, pas)



