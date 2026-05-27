#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,na ordem de colocação. 
#Depois mostre: a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
print('-----------------------------------')
print('   CAMPEONATO BRASILEIRO SÉRIE A 2026')
print('-----------------------------------')
campeonato = ('Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo','Athletico-PR', 'Bahia', 'Red Bull Bragantino', 'Vasco da Gama', 'Coritiba',
              'Vitória', 'Cruzeiro', 'Botafogo', 'Atlético-MG', 'Internacional', 'Santos', 'Corinthians', 'Grêmio', 'Mirassol', 'Remo', 'Chapecoense')
r=input(' A) ver os 5 primeiros colocados:\n '
'B) Ver os últimos 4 colocados:\n ' 
'C) Ver os times participantes em ordem alfabética:\n ' 
'D) Ver a posição do time CHAPECOENSE: \n'
' O que você quer fazer? ').upper()
if r == 'A':
    print('5 primeiros na colocação!')
    for cont in range (5):
        cont+=1
        print(f'{cont} {campeonato[cont]}')
    print('-----------------------------------')
elif r == 'B':
    print('Os 4 últimos colocados!')
    for cont in range(16, 20):
        print(f'{cont+1} {campeonato[cont]}')
    print('-----------------------------------')
elif r == 'C':
    print('Os times que estão no campeonato, em ordem alfabética: ')
    print(f'{sorted(campeonato)}')
elif r == 'D':
    print(f'A posição do Chapecoense no campeonato é {campeonato.index("Chapecoense") + 1}.')
else:
    print('ERRO')
