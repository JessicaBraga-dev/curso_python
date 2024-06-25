from random import randint
from time import sleep
from operator import itemgetter
dados = {'Jodador1': randint(1, 6),
         'Jogador2': randint(1, 6),
         'Jogador3': randint(1, 6),
         'Jogador4': randint(1, 6)}
ranking = list()
print(f'-=' * 8, 'NÚMEROS SORTEADOS', '-=' * 8)
for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)
print('-=' * 26)
print(f'-=' * 7, 'RANKING DOS JOGADORES', '-=' * 8)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]}')
    sleep(1)