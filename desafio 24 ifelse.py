distacia = float(input('Qual é a distância da sua viagem? '))
if distacia <= 200:
    print('Preço da sua passagem será de RS{:.2f}'.format(distacia * 0.50))
else:
    print('Preço da sua passagem será de RS{:.2f}'.format(distacia * 0.45))