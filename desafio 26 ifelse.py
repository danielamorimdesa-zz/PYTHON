salario = float(input('Qual o salário do funcionário: R$'))
novo15 = salario + (salario*15/100)
novo10 = salario + (salario*10/100)
if salario <= 1250:
    print('Quem ganhava R${:.2f} vai passar a ganahr um novo de salário: R${:.2f}'.format(salario,novo15))
else: 
    print('Quem ganhava R${:.2f} vai passar a ganahr um novo salário: R${:.2f}'.format(salario,novo10))