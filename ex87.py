ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'{"Nº":<5}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<5}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<<< VOLTE SEMPRE >>>>>')
