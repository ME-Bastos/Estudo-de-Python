#Ano de nascimento de um jovem, fala se ele ainda vai se alistar ao serviço militar (18 anos)
# se é a hora de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
nasc=int(input('Digite seu ano de nascimento: '))
idade= 2026-nasc
if idade < 18:
    ano = 18 - idade
    print (f'Você ainda não pode se alistar, faltam {ano} anos para poder se alistar.')
elif idade == 18:
    print ('Você está na idade de se alistar!')
else:
    ano = idade - 18
    print(f'Já passou da hora de se alistar! Deveria ter se alistado a {ano} atrás.')