from math import sin, cos, tan, radians

a = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(a,seno))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(a,cos))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}'.format(a,tan))