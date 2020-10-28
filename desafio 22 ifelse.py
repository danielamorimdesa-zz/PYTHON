velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade <= 80:
    print('Tenha um bom dia! Diriga com segurança.')
else:
    print('MULTADO. Você excedeu o limite permitido de 80km/h. Você deve pagar uma multa de R${:.2f}'.format(velocidade*7))