d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(d))
if d <= 200:
    v = d * 0.50
else:
    v = d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(v))

'''
d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f}Km.'.format(d))
v = d * 0.50 if d <= 200 else d * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(v))
'''

