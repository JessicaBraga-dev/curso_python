nome = str(input('DIGITE SEU NOME COMPLETO: ')).strip().upper()
n = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))