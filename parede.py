# o programa tem que ler as dimensões da parede, calcular sua área e a quantidade de tinta que precisa para pintar
# consideramos que cada litro de tinta pinta 2m^2
larg=float(input('Digite a largura da parede:'))
alt=float(input('Digite a altura da parede:'))
área= larg*alt
tinta = área / 2
#:.2f faz com que só tenha 2 números depois da virgula
print(f'Sua parede tem a dimensão de {larg:.2f} x {alt:.2f} e sua área é de {área:.2f} metros quadrados.')
print('-'*15)
print(f'Você precisará de {tinta}l de tinta.')
