n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para coversão:
[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
opcao = int(input('Opcão: '))
if opcao == 1:
    print('Binário: {}'.format(bin(n)[2:]))
elif opcao == 2:
    print('Octal: {}'.format(oct(n)[2:]))
elif opcao == 3:
    print('Hexadecimal: {}'.format(hex(n)[2:]))
else:
    print('Opção invalida')