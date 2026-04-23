# O computador “pensa” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
computador = randint (0,5)
print ('Jogo da adivinhação')
jog=int(input('Escreva um número de 0 a 5! '))
if jog==computador: 
    print (f'Você perdeu... O computador pensou em {computador}') 
else: 
    print (f'Você ganhou! O computador pensou no número {computador}')