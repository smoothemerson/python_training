minha_lista = [1, 2, 3, 4, 5]
print("Minhas lista de exemplo:", minha_lista)

minha_lista[0] = 1
print("Minhas lista de exemplo:", minha_lista)

minha_lista.append(6)
print("Após append(6):", minha_lista)

indice = minha_lista.index(6)
print("Índice do elemento 6:", indice)

minha_lista.insert(2, 10)
print("Após insert(2, 10):", minha_lista)

elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Após pop(3):", minha_lista)

minha_lista.remove(True)
print("Após remove(True):", minha_lista)

minha_lista.sort()
print("Após sort():", minha_lista)
