pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

print("Meu dicionário de exemplo: ", pessoa)
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])

pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])

del pessoa["cidade"]
print("Dicionário após remover a cidade:", pessoa)

chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)

valores = list(pessoa.values())
print("Valores do dicionário:", valores)

itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
