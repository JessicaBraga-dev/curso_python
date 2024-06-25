'''a = [2, 3, 4, 7]
#b = a
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista b: {b}')
'''
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)


for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for v in valores:
    print(f'{v}...', end='')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

































'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
num.insert(2, 2)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número quatro')
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número quatro')
print(f'Essa lista tem {len(num)} elementos')
print(num)'''














































'''LISTAS
lanche = ['hamburgue', 'Pizza', 'refri', 'Pudim'] →

lanche.append(cookies) → adiciona na lista
lanche.insert(0, 'cachorro quente') → adiciona na posição desejada
del lanche [3] → apagar elementos
lanche.pop(3) → geralmente apaga o último elemento, mas pode passar o parametro
lanche.remove('pizza') → remove pelo conteudo
lanche.pop() → remove o último
Caso queira remover algo, se ele não estiver na lista dará erro, entao se usa estrutura if
if pizza in lanche:
    lanche.remove('pizza')

valores = list(range(4,11))
valores.sort() → ordem menor p maior
valores.sort(reverse=True) → maior para menor
len(valores) → tamanho
'''
