# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
s1=float(input('Digite o seu salário atual: '))
if s1 > 1250:
    s2 = s1*10/100
    sf = s1 + s2
else:
    s2 = s1*15/100
    sf = s1 + s2
print(f'O seu novo salário agora será de R${sf:.2f}')
