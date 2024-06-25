def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if formato is False else moedas(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moedas(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moedas(res)


def aumento(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa/10)
    return res if formato is False else moedas(res)


def moedas(preco=0, moedas='R$'):
    return f'{moedas}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moedas(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumento(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preco, taxar, True)}')
