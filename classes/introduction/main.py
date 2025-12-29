nome = "Emerson"
nome_com_x = "xEmersonx"
sobrenome = "Rocha"
nome_completo = "Emerson Rocha"

print(f"Contagem do caractere e: {nome_completo.count('e')}")
print(f"Posição do caractere R: {nome_completo.find('R')}")
print(f"Encodificação: {nome_completo.encode()}")
print(f"Decodificação: {nome_completo.encode().decode()}")
print(f"Substituição do caractere o por 0: {nome_completo.replace('o', '0')}")
print(f"Adicionar separador entre nome: {'-'.join(nome)}")
print(f"Dividir nome completo pelo espaço: {nome_completo.split(' ')}")
print(f"Remover caracteres x do nome alvo: {nome_com_x.strip('x')}")
print(f"Remover caracteres x da direita do nome alvo: {nome_com_x.rstrip('x')}")
print(f"Remover caracteres x da esquerda do nome alvo: {nome_com_x.lstrip('x')}")
print(f"Verifica se o nome completo começa com Eme: {nome_completo.startswith('Eme')}")
print(f"Verifica se o nome completo contém cha: {'cha' in nome_completo}")
print(f"Verifica se o nome completo não contém abc: {'abc' not in nome_completo}")
