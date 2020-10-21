preco = float(input('Preço do produto: R$'))
vdesconto = preco * 5 / 100
desconto = preco - vdesconto
print('O produto custava R${}, na promoção com 5% vai custar R${:.2f}'.format(preco,desconto))
