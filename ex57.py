import time
v1 = int(input('DIGITE PRIMEIRO VALOR: '))
v2 = int(input('DIGITE SEGUNDO VALOR: '))
while True:
    print('[ 1 ] SOMAR\n'
          '[ 2 ] MULTIPLICADOR\n'
          '[ 3 ] MAIOR\n'
          '[ 4 ] NOVOS NÚMEROS\n'
          '[ 5 ] SAIR DO PROGRAMA')
    r = int(input('>>>> Qual é a sua opção? '))
    if r == 1:
        print('A soma entre {} + {} é {}'.format(v1, v2, v1+v2))
    elif r == 2:
        print('O resultado de {} x {} é {}'.format(v1, v2, v1*v2))
    elif r == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('Entre {} e {} o maior é {}'.format(v1, v2, maior))
    elif r == 4:
        print('Informe os números novamente:')
        v1 = int(input('DIGITE PRIMEIRO VALOR: '))
        v2 = int(input('DIGITE SEGUNDO VALOR: '))
    elif r == 5:
        print('FINALIZANDO...')
        time.sleep(1)
        print('-==-'*10)
        print('Fim do programa! Volte sempre!')
        break
    else:
        print('Opção inválida. Tente novamente')



'''v1 = int(input('DIGITE PRIMEIRO VALOR: '))
v2 = int(input('DIGITE SEGUNDO VALOR: '))
opcao = 0
while opcao != 5:
    print('[ 1 ] SOMAR\n'
          '[ 2 ] MULTIPLICADOR\n'
          '[ 3 ] MAIOR\n'
          '[ 4 ] NOVOS NÚMEROS\n'
          '[ 5 ] SAIR DO PROGRAMA')
    opcao = int(input('>>>> Qual é a sua opção? '))
    if opcao == 1:
        soma = v1 + v2
        print('A soma entre {} + {} é {}'.format(v1, v2, soma))
    elif opcao == 2:
        mul = v1 * v2
        print('O resultado de {} x {} é {}'.format(v1, v2, mul))
    elif opcao == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('Entre {} e {} o maior é {}'.format(v1, v2, maior))
    elif opcao == 4:
        print('Informe os números novamente:')
        v1 = int(input('DIGITE PRIMEIRO VALOR: '))
        v2 = int(input('DIGITE SEGUNDO VALOR: '))
    elif opcao == 5:
        print('FINALIZANDO...')
        print('-==-'*10)   
    else:
        print('Opção inválida. Tente novamente')
    print('Fim do programa! Volte sempre!')'''





