from ex108 import moedas

p = float(input('Digite um preço:  R$'))
print(f'A metade de {moedas.moedas(p)} é {moedas.moedas(moedas.metade(p))}')
print(f'O dobro de {moedas.moedas(p)} é {moedas.moedas(moedas.dobro(p))}')
print(f'Aumentando 10% temos {moedas.moedas(moedas.aumento(p, 10))}')

