from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('ANO DE NASCIMENTO: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('CARTEIRA DE TRABALHO: (0 NÃO TEM) '))
if dados['ctps'] != 0:
    dados['contrataçao'] = int(input('ANO DE CONTRATAÇÃO: '))
    dados['salario'] = float(input('SALÁRIO: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contrataçao'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
