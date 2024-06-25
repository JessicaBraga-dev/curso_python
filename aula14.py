galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    #galera.append(dado) >>> outro resultado
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')








'''galera = [['Marco', 9], ['Bernardo', 6], ['Juliana', 14], ['Jéssica', 31],]
for p in galera:
    print(p)
    print(p[0])
    print(p[1])
    print(f'{p[0]} tem {p[1]} anos de idade.')'''






'''galera = [['Marco', 9], ['Bernardo', 6], ['Juliana', 14], ['Jéssica', 31],]
print(galera[0])
print(galera[0][1])
print(galera[3][1])
print(galera[2][0])
print(galera[3][0])
print(galera[0][0])
print(galera[2][1])'''






















''''teste = list()
teste.append('Jéssica')
teste.append(30)
galera = list()
#galera.append(teste) sem os dois pontos faz uma ligação entre as listas
galera.append(teste[:])#faz uma copia com dois pontos
teste[0] = 'Marco'
teste[1] = 9
galera.append(teste[:])
print(galera)'''
