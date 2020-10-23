from math import sin,cos,tan,radians

angulo = float(input("Digite o ângulo que você deseja: "))
print('Seno: {:.2f}'.format(sin(radians(angulo))))
print('Consseno: {:.2f}'.format(cos(radians(angulo))))
print('Tangente: {:.2f}'.format(tan(radians(angulo))))