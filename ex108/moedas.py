def diminuir(preço=0, taxa=0):
    res = preço - (preço * taxa/100)
    return res


def metade(preço=0):
    res = preço / 2
    return res


def dobro(preço=0):
    res = preço * 2
    return res


def aumento(preço=0, taxa=0):
    res = preço + (preço * taxa/10)
    return res


def moedas(preço=0, moedas='R$'):
    return f'{moedas}{preço:>.2f}'.replace('.', ',')