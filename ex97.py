from time import sleep


def maior(* num):
    cont = maior = 0
    print('-=' * 50)
    print('\nAnalizando os valores passados ...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


#Programa principal
maior(9, 10, 5, 8, 2, 3)
maior(1, 2)
maior(-1, 0)
maior(2, 8)
maior(8, 7, 5, 4)
maior(1, 3, 9)
maior(0)
maior(8, 2)
maior(10, 1)