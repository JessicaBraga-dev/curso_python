from random import shuffle
p1 = str(input('Primeiro: '))
p2 = str(input('Segundo: '))
p3 = str(input('Terceiro: '))
p4 = str(input('Quarta: '))
lista = [p1,p2,p3,p4]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))