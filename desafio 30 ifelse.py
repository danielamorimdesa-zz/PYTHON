from datetime import date
atual = date.today().year
ano = int(input('Qual seu ano de nascimento: '))
idade = atual - ano
if idade == 18:
    print('Você tem que se alistar imediatamente')
elif idade < 18:
    print('Falta {} anos para o alistamento'.format(18 - idade))
elif idade > 18:
    print('Deveria ter se alistado há {} anos'.format(idade - 18))