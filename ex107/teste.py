from ex107 import moedas

p = float(input('Digite um preço: R$ '))
print(f'A metade de R${p} é R${moedas.metade(p)}')
print(f'O dobro de R${p} é R${moedas.dobro(p)}')
print(f'Aumentando 10% temos {moedas.aumento(p, 10)}')
print(f'Diminuindo 20% temos {moedas.diminuir(p, 20)}')
