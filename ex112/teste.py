from ex112.utilidades import moedas
from ex112.utilidades import dados

p = dados.leiaDinheiro('Digite o preço:  R$')
moedas.resumo(p, 20, 10)
