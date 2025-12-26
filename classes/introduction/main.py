nome_completo = "Emerson Rocha"

nome_completo_aspas = """Emerson
Rocha"""

nome_completo_quebra = "Emerson \
Rocha"

nome = "Emerson"
sobrenome = "Rocha"

print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma): " + nome_completo)
print("Nome completo (3a forma): " + "Emerson " + "Rocha")
print("Nome completo (4a forma): " + "Emerson", "Rocha")
print("Nome completo (5a forma): " + nome_completo_aspas)
print("Nome completo (6a forma): " + nome_completo_quebra)
print("Nome completo (7a forma): %s" % nome_completo)
print("Nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma): {nome} {sobrenome}")
print("Nome completo (9a forma): {} {}".format(nome, sobrenome))
