from random import randint
from time import sleep

def sorteio(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} → ', end='')
        sleep(0.5)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Sorteando os valores pares de {lista}, temos {soma}')



#Programa principal
num = list()
sorteio(num)
somaPar(num)

