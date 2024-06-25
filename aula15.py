estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).upper()
    estado['sigla'] = str(input('Sigla do Estado: ')).upper()
    #brasil.append(estado) vai repitir o primeiro resultado
    #brasil.append(estado[:]) esse tipo de copia só serve nas listas
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()



'''    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')'''

    #print(e)






















'''brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla': 'RJ'}
estado2 ={'uf':'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''



























'''pessoas = {'nome': 'Jéssica', 'Sexo': 'M', 'idade': 31}
pessoas['nome'] = 'Juliana'
pessoas['peso'] = 98.5
del pessoas['Sexo']
print(pessoas)
#print(pessoas[0]) em dicionarios as posição são chamadas pelos nomes
print(pessoas['nome'])
print(pessoas['idade'])
print(f'A {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(f'{k} = {v}')'''