#Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.
v=int(input('Qual a velocidade atual do seu carro? '))
if v>=80:
    multa=(v-80)*7
    print(f'Você está acima da velocidade permitida! A multa é de {multa} reais.')
else:
    print('Parabéns! Você está na velocidade permitida')