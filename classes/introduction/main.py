lista = [1, 2, 3, 4, 5]

print("For utilizando lista")
for elemento in lista:
    print(elemento)

tupla = (1, 2, 3, 4, 5)

print("\nFor utilizando tupla")
for elemento in tupla:
    print(elemento)

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

print("\nFor utilizando dicionário - chaves")
for chave in pessoa.keys():
    print(chave)

print("\nFor utilizando dicionário - valores")
for valor in pessoa.values():
    print(valor)

print("\nFor utilizando dicionário - items")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")
