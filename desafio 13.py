n1 = float(input('Salário do funcionário: R$'))
aumento = n1 * 15 / 100
naumento = n1 + aumento
print('Funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(n1,naumento))