#jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
total = jogador = v = 0
tipo = ''
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 11)
    total = jogador + computador

    tipo = ''
    while tipo not in ('P', 'I'):
        tipo=input('Par ou Impar? [P/I] ').strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, o total ficou {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VITÓRIA')
            v += 1
        else:
            print('DERROTA')
            break
    else:
        if total % 2 == 1:
            print('VITÓRIA')
            v += 1
        else:
            print('DERROTA')
            break
print(f'Você ganhou {v} vezes consecutivas do computador.')
