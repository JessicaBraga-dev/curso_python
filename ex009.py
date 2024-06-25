l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
area = l * a
print('Essa parede tem a dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².'.format(l,a,area))
print('Para pintar essa parede, você precisará de {:.2f}litros de tinta.'.format(area/2))