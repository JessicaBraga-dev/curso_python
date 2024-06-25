pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [F/M] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas F ou M.')
    pessoa['idade'] = int(input('Idade : '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas com S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'B) A média de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'D) Listas ne pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} => {v};  ', end='')
        print()
print('>>> ENCERRANDO <<<')