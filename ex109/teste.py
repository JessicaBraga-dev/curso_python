from ex109 import moedas

p = float(input('Digite um preço:  R$'))
print(f'A metade de {moedas.moedas(p)} é {moedas.metade(p, True)}')
print(f'O dobro de {moedas.moedas(p)} é {moedas.dobro(p, True)}')
print(f'Aumentando 10% temos {moedas.aumento(p, 10, True)}')

