num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if num == 3:
       print(f'O valor 3 apareceu na {num.index(3)}ª posição')
else:
       print('Valor não encontrado')
print(f'Os valores pares digitados foram ', end=' ')
for n in num:
       if n % 2 == 0:
              print(n, end=' ')
