n = bool(input('Digite um valor: '))
print(n)

#--------------------------------------------------------------
n = float(input('Digite um valor: '))
print(n)

#--------------------------------------------------------------
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma vale', s)
print('A soma entre {} e {} vale {}'.format(n1,n2,s))
print('A Soma entre ', n1,'e ',n2,'vale ',s)

#Sem o tipo primitivo int a string não soma , concatena ex: 5 + 5 = 55
#--------------------------------------------------------------
#type
n1 = input('Digite um valor: ')
print(type(n1))