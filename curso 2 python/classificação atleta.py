#Leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos: MIRIM; Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR; Até 25 anos: SÊNIOR; Acima de 25 anos: MASTER
nasc=int(input('Digite o ano do seu nascimento: '))
idade = 2026 - nasc
if idade <= 9:
    print('VOCÊ ESTÁ NA CATEGORIA MIRIM')
elif idade > 9 and idade <= 14:
    print('VOCÊ ESTÁ NA CATEGORIA INFANTIL')
elif idade > 14 and idade <= 19:
    print('VOCÊ ESTÁ NA CATEGORIA JUNIOR')
elif idade > 19 and idade <= 25:
    print('VOCÊ ESTÁ NA CATEGORIA SÊNIOR')
else:
    print('VOCÊ ESTÁ NA CATEGORIA MASTER')