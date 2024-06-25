jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f' Quantas partidas {jogador["nome"]} jogou ?' ))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas com S ou N.')
    if resp == 'N':
        break
print('-=' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 60)
while True:
    bus = int(input('Mostra dados de qual jogador? (999 para parar) '))
    if bus == 999:
        break
    if bus >= len(time):
        print(f'ERRO! Não existe jogador com código {bus}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[bus]["nome"]}:')
        for i, g in enumerate(time[bus]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')



'''    for k, v in jogador.items():
        print(f'O campo {k} tem o valor {v}')
    print('-=' * 30)
    print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
    for i, v in enumerate(jogador['gols']):
        print(f'   → Na partida {i+1}, fez {v} de gols.')
    print(f'Foi um total de {jogador["total"]} gols')'''