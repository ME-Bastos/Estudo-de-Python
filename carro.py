# Crie um dicionário chamado carro com as chaves modelo, ano e cor. Depois, mude o ano do carro acessando a chave.
carro = {
    "modelo":"Porsche 911",
    "ano": 2023,
    "cor": "prata"
}
print(carro['modelo'])
print(carro['ano'])
carro['ano'] = 2024
print(carro['ano'])