l1 = float(input('PRIMEIRO SEGMENTO: '))
l2 = float(input('SEGUNDO SEGMENTO: '))
l3 = float(input('TERCEIRO SEGMENTO: '))


if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima PODEM FORMAR um TRIÂNGULO ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIÂNGULO')







'''
if l1 == l2 and l2 == l3:
    print('EQUILÁTERO')
if l1 != l2 and l2 != l3 and l1 != l3:  
     print('ESCALENO')
'''