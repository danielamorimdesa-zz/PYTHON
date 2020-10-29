vcasa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
prestacao = vcasa / (anos * 12)
minimo = salario * 30 / 100
if prestacao <= minimo:
    print('APROVADO. Parcela R${:.2f}'.format(prestacao))
else:
    print('NEGADO')