# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
v=int(input('Quantos kilometros são a viagem? '))
if v <= 200:
    p = v*0.50
    print(f'O preço da passagem fica {p} reais')
else:
    p = v*0.45
    print(f'O preço da passagem fica {p} reais')