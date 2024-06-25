somar = cont = 0
while True:
    num = int(input('DIGITE UM VALOR  (999 PARA PARAR): '))
    if num == 999:
        break
    somar += num
    cont += 1
print(f'A soma dos {cont} foi {somar}!')