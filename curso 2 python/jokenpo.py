#Crie um programa que faça o computador jogar Jokenpô com você
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2)
print('Suas opções: \n [0] Pedra \n [1] Papel \n [2] Tesoura:')
jogador=int(input('Qual a sua jogada? '))
print(f'O jogador jogou {itens[jogador]}')
print(f'O computador jogou {itens[computador]}')
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('VITÓRIA!')
    elif jogador == 2:
        print('DERROTA')
    else:
        print('INVÁLIDO')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('DERROTA')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('VITÓRIA!')
    else:
        print('INVÁLIDO')
else: #computador jogou tesoura
    if jogador == 0:
        print('VITÓRIA!')
    elif jogador == 1:
        print('DERROTA')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('INVÁLIDO')