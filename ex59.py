print('GERADOR DE PA')
print('-='*15)
p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
t = p
c = 1

while c <= 10:
    print('{} → '.format(t), end='')
    t += r
    c += 1
print('FIM!')
