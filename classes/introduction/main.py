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

print("\nUtilizando a função range()")
for numero in range(5):
    print("\nNúmero: ", numero)

print("\nUtilizando a função range() com len()")
lista = [1, 2, 3, 4, 5, 6]
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = 5
    else:
        lista[indice] = 0
print(lista)

lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
    if indice == 1:
        print("Índice 1")
