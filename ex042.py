print('======================================== MERCADINHO DO BE ========================================')
preco = float(input('PREÇO DAS COMPRAS: R$ '))
print('FORMA DE PAGAMENTO \n '
      '[ 1 ] à vista dinheiro/cheque \n '
      '[ 2 ] à vista cartão \n '
      '[ 3 ] 2x no cartão \n '
      '[ 4 ] 3x ou mais no cartão')
opcao = int(input('OPÇÃO: '))
par = preco + (preco*20/100)

if opcao == 1:
    print('Sua compra de R${} vai custar R${} no final.'.format(preco,preco - (preco*10/100)))
elif opcao == 2:
    print('Sua compra de R${} vai custar R${} no final.'.format(preco,preco - (preco*5/100)))
elif opcao == 3:
    print('Sua compra será parcelas em 2x de R${}'.format(preco/2))
elif opcao == 4:
    div = int(input('PARCELAS: '))
    print('Sua compra será parcelada me {}x de R${} COM JUROS'.format(div,par/div))
    print('Sua compra de R${} vai custar R${} no final.'.format(preco,par))
else:
    print('Opção INVÁLIDA!')
'''
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total/2
    print('Sua compra foi parcelada em R${}'.format(parcela))
elif opcao == 4:
    total = preco - (preco * 20 / 100)
    div = int(input('PARCELAS: '))
    totalpar = par / div
print('Sua compra de R${} vai custar R${} no final.'.format(preco,total))
    
'''