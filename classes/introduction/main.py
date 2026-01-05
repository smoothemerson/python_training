idade = int(input("Quantos anos você tem? "))

if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 12:
    print("Você é um adolescente")
else:
    print("Você é menor de idade.")

print(
    "Pode tirar a carteira de habilitação"
    if idade >= 18
    else "Não pode tirar a carteira de habilitação"
)
