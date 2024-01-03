from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo que voce deseja: '))

seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Seno e: {:.2f}'.format(seno))
print('Coseno e: {:.2f}'.format(coseno))
print('Tangente e: {:.2f}'.format(tangente))