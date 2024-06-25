camp = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo',
        'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR',
        'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá',
        'Corinthians', 'Cruzeiro', 'Vasco da Gama', 'Bahia',
        'Santos', 'Goiás', 'Coritiba', 'América-MG', 'Chapecoense')
print(f'Lista de Times do BRASILEIRÃO: {camp}')
print('-='*100)
print(f'Os 5 primeiros times: {camp[:5]}')
print('-='*100)
print(f'Os últimos 4 colocados: {camp[-4:]}')
print('-='*100)
print(f'Times em ordem alfabética: {sorted(camp)}')
print('-='*100)
print(f'O Chapecoense está na {camp.index("Chapecoense")+1}ª posição')
