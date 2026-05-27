#leia o ano de nascimento de sete pessoas. Mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
maior=0
menor=0
for c in range (1, 8):
    nasc=int(input(f'Digite o ano de nascimento da {c} pessoa: '))
    idade= 2026-nasc
    if idade >= 18:
        maior+=1
    else:
        menor+=1
    c +=1
print(f'Entre as sete pessoas mencionadas, {maior} são maiores de idade e {menor} são menores de idade')
