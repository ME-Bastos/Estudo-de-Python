#Calcule seu IMC peso/(altura x altura) e mostre seu status, de acordo com a tabela abaixo: abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal; 25 até 30: Sobrepeso; 30 até 40: Obesidade; Acima de 40: Obesidade Mórbida
peso=float(input('Digite o seu peso atual: '))
alt=float(input('Digite a sua altura atual: '))
IMC = peso/(alt*alt)
if IMC < 18.5:
    print('Você está abaixo do peso.')
elif IMC > 18.5 and IMC < 25:
    print('Você está no peso ideal.')
elif IMC > 25 and IMC < 30:
    print('Você está em sobrepeso.')
elif IMC > 30 and IMC < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')