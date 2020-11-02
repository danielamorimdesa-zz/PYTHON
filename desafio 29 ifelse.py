try:
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
   
    if n1 > n2:
        print('O maior é {}'.format(n1))
    elif n1 < n2:
        print('Maior é {}'.format(n2))
    elif n1 == n2:
        print('São iguais')
except ValueError:
     print('VALOR INVALIDO')