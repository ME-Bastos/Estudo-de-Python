#Lê o nome de alguém
# – O nome com todas as letras maiúsculas e minúsculas. Quantas letras ao todo (sem considerar espaços). Quantas letras tem o primeiro nome.
nome=str(input('Digite seu nome: ')).strip()
print(f'Nome em caixa alta: {nome.upper()}')
print(f'Nome em caixa baixa: {nome.lower()}')
print(f'Quantas letras tem: {len(nome) - nome.count (' ')}') # - nome.count (' ') "pula" os espaços 
print(f'Quantas letras tem no primeiro nome: {nome.find(' ')}') # o nome.find vai até o primeiro espaço, por isso conta só o primeiro nome