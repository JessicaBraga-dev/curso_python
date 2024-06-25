print('GERADOR DE PA')
print('-='*15)
p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
t = p
c = 1
tot = 0
m = 10
while m != 0:
    tot += m
    while c <= tot:
        print('{} → '.format(t), end='')
        t += r
        c += 1
    print('PAUSA!')
    m = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(tot))
print('FIM!')
