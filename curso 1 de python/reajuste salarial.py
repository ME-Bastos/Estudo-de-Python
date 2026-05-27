# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s1=float(input('Digite o seu salário atual:'))
aumento=s1*15/100
s2=s1+aumento
print(f'Seu novo salário será de R${s2:.2f}')