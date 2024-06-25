print('-=-'*50)
print('ANALIZADOR DE TRIÂNGULOS')
print('-=-'*50)

r1 = float(input('PRIMEIRO SEGMENTO: '))
r2 = float(input('SEGUNDO SEGMENTO: '))
r3 = float(input('TERCEIRO SEGMENTO: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')



















