cores = {
'''ex:['amarelo']['limpa']'''
         'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'
}
print('\033[33m-=-=-\033[m'*50)
print('APROVANDO EMPÉSTIMO ...')
print('\033[33m-=-=-\033[m'*50)
cs = float(input('VALOR DA CASA: R$ '))
sal = float(input('SALÁRIO DO COMPRADOR: R$ '))
fin = int(input('QUANTOS ANOS DE FINANCIAMENTO: R$ '))
print('\033[33m-=-=-\033[m'*50)
p = cs / (fin * 12)
min = sal * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos. '.format(cs, fin), end='')
print('a prestação será de R${:.2f} '.format(p))
if p <= min:
    print('EMPRÉSTIMO PODE SER \033[34mCONCEDIDO\033[m !')
else:
    print('EMPRÉSTIMO \033[31mNEGADO\033[m ! ')
print('\033[33m-=-=-\033[m'*50)




