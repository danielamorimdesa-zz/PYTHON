from random import randint
numero = randint(0,5)
print('Vou pensar em um número de O a 5. Tente advinhar.')
print('-'*60)
numero1 = int(input('Em que número eu pensei? '))
print('-'*60)
if numero == numero1:
    print('VOCÊ VENCEU')
else:
    print('VOCÊ PERDEU')