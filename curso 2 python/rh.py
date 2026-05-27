#Crie uma lista chamada funcionarios contendo pelo menos 3 dicionários (invente os nomes e cargos).
#Um dos funcionários recebeu uma promoção! Acesse esse funcionário na lista e mude o cargo dele para "Gerente" e aumente o salario em 2000.
#Use um laço for para imprimir a ficha de cada um no formato:
# "O funcionário [NOME] trabalha como [CARGO] e ganha R$[SALARIO]."
rh = [
    {"Nome": "Maria", "Cargo" : "Recrutador", "Salario" : 2000.00},
    {"Nome": "João", "Cargo" : "Analista de RH", "Salario" : 2300.00},
    {"Nome": "Luisa", "Cargo" : "Coordenador", "Salario" : 2500.00},
]
for funcionario in rh:
    if funcionario ['Nome'] == 'Luisa':
        funcionario ['Cargo'] = 'Gerente'
        funcionario ['Salario'] += 2000.00

for funcionario in rh:
    print(f'O funcionario {funcionario['Nome']} trabalha como {funcionario['Cargo']} e ganha R${funcionario['Salario']}')