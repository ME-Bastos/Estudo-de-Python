#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
C=float(input('Quantos graus está agora? '))
# C × 9/5) + 32 = °F -> conta de celsius pra fahrenheit
F = (C * 9/5) + 32
print(F'Convertendo para Fahrenheit, agora estaria {F} °F')
