dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
total = (dias * 60) + (km * 0.15)
print('Total a pagar é de R${}'.format(total))