
vel = float(input('Qual a velocidade do carro:km/h '))
if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é 80km/h.\nVocê deve pagar uma multa de R${:.2f} !'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
