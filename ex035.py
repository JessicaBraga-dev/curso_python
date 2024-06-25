import math
num = int(input('DIGITE UM NÚMERO INTEIRO: '))
print('[ 1 ] Converter para BINÁRIO ')
print('[ 2 ] Converter para OCTAL ')
print('[ 3 ] Converter para HEXADECIMAL ')
escolha = int(input('ESCOLHA UMA DAS BASES PARA CONVERSÃO: '))
bi = bin(num)[2:]
oc = oct(num)[2:]
he = hex(num)[2:]
if escolha == 1:
    print('Sua opção: 1')
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bi))
elif escolha == 2:
    print('Sua opção: 2')
    print('{} convertido para OCTAL é igual a {}'.format(num,oc))
elif escolha == 3:
    print('Sua opção: 3')
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,he))
else:
    print('OPÇÃO INVÁLIDA. Por favor escolha uma das opções acima')

