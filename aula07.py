'''a = 5
b = 6
print('Os valores são \033[32m{}\033[m e \033[36m{}\033[m'.format(a,b))'''

'''print('\033[4;30;45mOlá Mundo!\033[m')
print('\033[7;33;44mOlá Mundo!\033[m')'''

nome = 'Jéssica'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}

print('Olá! Muito Prazer em te conhecer {}{}{}' .format('\033[4;34m', nome, '\033[m'))
print('Olá! Muito Prazer em te conhecer {}{}{}' .format(cores['amarelo'], nome, cores['limpa']))