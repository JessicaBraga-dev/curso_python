print('\033[32:1mCALCULANDO O ÍNDICE DE MASSA CORPORAL (IMC)\033[m')
print('\033[33m-=-=-\033[m'*50)

peso = float(input('\033[32:1mDIGITE SEU PESO:(Kg) \033[m'))
alt = float(input('\033[32:1mDIGITE SUA ALTURA: (M) \033[m'))
print('\033[33m-=-=-\033[m'*50)
imc = peso / (alt**2)

print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif imc >= 25 and imc < 30:
    print('Você está SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, CUIDADO!')

'''
elif 18.5 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
'''