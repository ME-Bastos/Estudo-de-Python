# O computador “pensa” em um número inteiro entre 0 e 5 e peça para o usuário tentar falar um número diferente do escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
computador = randint (0,10)
print ('Jogo da adivinhação')
jog = 'ERROU'
#jog=int(input('Escreva um número de 0 a 5! '))
#if jog==computador: 
#    print (f'Você perdeu... O computador pensou em {computador}') 
#else: 
#    print (f'Você ganhou! O computador pensou no número {computador}') código do jogo anterior

#vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer

while jog == 'ERROU':
    jog=int(input('Digite o número que você acha que o computador digitou de 0 a 10: '))
    if jog == computador:
        print('Parabéns, você adivinhou o número!')
    else:
        print('Você errou, tente novamente.')
        jog = 'ERROU'
