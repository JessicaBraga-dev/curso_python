'''n1 = int(input('DIGITE PRIMEIRO VALOR: '))
n2 = int(input('DIGITE SEGUNDO VALOR: '))
n3 = int(input('DIGITE TERCEIRO VALOR: '))
menor = min(n1,n2,n3)
maior = max(n1,n2,n3)
print('O MENOR valor digitado foi {}'.format(menor))
print('O MAIOR valor digitado foi {}'.format(maior))'''

n1 = int(input('DIGITE PRIMEIRO VALOR: '))
n2 = int(input('DIGITE SEGUNDO VALOR: '))
n3 = int(input('DIGITE TERCEIRO VALOR: '))

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
'-------------------------------------------------------'
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O MENOR valor digitado foi {}'.format(menor))
print('O MAIOR valor digitado foi {}'.format(maior))
