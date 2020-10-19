n1 = int(input('Digite um número para ver sua tabuada: '))
for i in range(1,11,1):
    mult = n1 * i
    print('{} x {} = {}'.format(i,n1,mult))
    i=i+1