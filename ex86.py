from random import randint
from time import sleep

print('-=' * 25)
print('                 JOGOS MEGA SENA             ')
print('-=' * 25)
sortlist = list()
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in sortlist:
            sortlist.append(num)
            cont += 1
        if cont >= 6:
            break
    sortlist.sort()
    jogos.append(sortlist[:])
    sortlist.clear()
    tot += 1
print('-=' * 7, f'SORTEANDO {quant} JOGOS', '-=' * 8)
sleep(2)
for i, l in enumerate(jogos):
    print(f'Jogos {i+1}: {l}')
print('-=' * 9, ' BOA SORTE! ', '-=' * 9)
