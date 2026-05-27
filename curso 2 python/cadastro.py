# Leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
m18 = tM = Fmenor20 = 0
while True:
    idade=int(input('Digite a idade da pessoa: '))
    sexo=input('Digite o sexo da pesssoa [M/F]: ').strip().upper()
    if idade >= 18:
        m18 += 1
    elif sexo == 'M':
        tM += 1
    elif sexo == 'F' and idade < 20:
        Fmenor20 += 1
    r=input('Quer continuar digitando? [S/N] ').strip().upper()
    if r == 'N':
        break
print(f'Entre os dados digitados, tem {m18} maiores de idade, foram cadastrados {tM} homens e {Fmenor20} mulheres tem menos de 20 anos.')