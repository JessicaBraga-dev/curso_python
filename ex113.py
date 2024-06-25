def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada interrompida pelo usuário.\33[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO!por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[31mEntrada interrompida pelo usuário.\033[m')
        else:
            return n


n1 = leiaInt('Digite um valor: ')
n2 = leiafloat('Digite um real: ')
print(f'O valor inteiro digitado foi {n1}, e o real {n2}')