def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('DIGITE UM NÚMERO: '))
if par(num):
    print('É PAR!')
else:
    print('NÃO É PAR!')
















'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os resultados são {f1}, {f2} e {f3}')'''
















































'''>>>>>>>>RETORNO VALORES(RETURN)<<<<<<
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


#Programa principal
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3}')'''


'''>>>>>>ESCOPO DE VARIÁVEIS <<<<<
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
#Programa principal
n = 2
print(f'No programa principal, n vale{n}')
teste()
print(f'No programa principal, x vale {x}')

#escopo local
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')


#Programa principal
#escopo global
n1 = 2
print(f'N1 global vale {n1}')


#Escopo local
def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')


#Programa principal
#Escopo global
a = 5
teste(a)
print(f'A fora vale {a}')'''


'''>>>>>>PARÂMETROS OPCIONAIS<<<<<<<<<


def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}', end='')
    

somar(3, 2, 5)
somar(8, 4)
somar()
somar(3)
somar(b=4, c=2)
somar(c=3, a=2)'''


'''>>>>INTERACTIVE HELP<<<<
#help(print) primeira maneira para ver manual das funcionalidades
# pythonconsole digite help() e para sair quit()
print(input.__doc__)
help(input)'''


'''
>>>>>>DOCSTRINGS<<<<<<<
def contador(i, f, p):
    """
    > Faz uma contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo do contador
    :return: sem retorno
    Função criada por Jéssica
    """
    c = 1
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(0, 100, 10)
help(contador)'''
