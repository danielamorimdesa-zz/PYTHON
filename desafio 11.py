larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m². Para pintar essa parede, você precisará de {}l tinta.'.format(larg,alt,area,tinta))