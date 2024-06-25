'''n = int(input('Digite um número para calcular seu Fatorial: '))
f = 0
print('Calculando {}! = '.format(n), end='')
for c in range(n, f, -1):
    print('{}'.format(c), end=' ')
    if c > 1:
        print('x ', end='')
    else:
        print(' =')'''






'''numero = int(input("Digite um número para calcular o fatorial: "))

# Verificar se o número é negativo
if numero < 0:
    print("Não é possível calcular o fatorial de números negativos.")
else:
    resultado = 1
    # Calcular o fatorial usando um loop for
    for i in range(1, numero + 1):
        resultado *= i
    print("O fatorial de", numero, "é:", resultado)'''