print('='*50)
print('10 TERMOS DE UMA PA')
print('='*50)
p = int(input('PRIMEIRO TERMO: '))
r = int(input('RAZÃO: '))
d = p + (10-1) * r
for c in range(p,d +r,r):
    print('{}'.format(c), end=' > ')
print('FIM!')