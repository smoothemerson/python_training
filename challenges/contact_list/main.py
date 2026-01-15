def adicionar_contato(contatos: list, nome: str, telefone: str, email: str):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"\n✅ Contato {nome} foi adicionado com sucesso!")
    return


def ver_contatos(contatos: list):
    print("\nLista de contatos:")
    if not contatos:
        print("Sua agenda está vazia.")
        return
    for indice, contato in enumerate(contatos, start=1):
        status = "⭐" if contato["favorito"] else " "
        print(
            f"{indice}. [{status}] {contato['nome']} | Tel: {contato['telefone']} | Email: {contato['email']}"
        )
    return


def atualizar_contato(
    contatos: list,
    indice_contato: str,
    novo_nome: str,
    novo_telefone: str,
    novo_email: str,
):
    try:
        indice_ajustado = int(indice_contato) - 1
        if 0 <= indice_ajustado < len(contatos):
            contatos[indice_ajustado]["nome"] = novo_nome
            contatos[indice_ajustado]["telefone"] = novo_telefone
            contatos[indice_ajustado]["email"] = novo_email
            print(f"\n✅ Contato {indice_contato} atualizado com sucesso!")
        else:
            print("\n❌ Índice de contato inválido.")
    except ValueError:
        print("\n❌ Por favor, digite um número válido para o índice.")
    return


def alternar_contato_favorito(contatos: list, indice_contato: str):
    try:
        indice_contato_ajustado = int(indice_contato) - 1
        if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
            contatos[indice_contato_ajustado]["favorito"] = not contatos[
                indice_contato_ajustado
            ]["favorito"]
            print(
                f"Contato {indice_contato} marcado/desmarcado como favorito com sucesso!"
            )
        else:
            print("Índice de contato inválido.")
    except ValueError:
        print("\n❌ Por favor, digite um número válido para o índice.")
    return


def ver_contatos_favoritos(contatos: list):
    print("\nLista de contatos favoritos:")
    favoritos = [c for c in contatos if c["favorito"]]
    if not favoritos:
        print("Nenhum contato favorito na sua agenda.")
        return
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            print(
                f"{indice}. [⭐] {contato['nome']} | Tel: {contato['telefone']} | Email: {contato['email']}"
            )
    return


def deletar_contato(contatos: list, indice_contato: str):
    try:
        indice_ajustado = int(indice_contato) - 1
        if 0 <= indice_ajustado < len(contatos):
            contato_removido = contatos.pop(indice_ajustado)
            print(f"Contato {contato_removido['nome']} foi deletado com sucesso")
        else:
            print("Índice inválido.")
    except ValueError:
        print("\n❌ Por favor, digite um número válido para o índice.")
    return


contatos = []

while True:
    print("\n--- Agenda de Contatos ---")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Atualizar contato")
    print("4. Marcar/desmarcar contato como favorito")
    print("5. Ver contatos favoritos")
    print("6. Deletar contato")
    print("7. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")
        adicionar_contato(contatos, nome, telefone, email)

    elif escolha == "2":
        ver_contatos(contatos)

    elif escolha == "3":
        ver_contatos(contatos)
        if contatos:
            indice = input("Digite o número do contato que deseja atualizar: ")
            nome = input("Digite o novo nome: ")
            telefone = input("Digite o novo telefone: ")
            email = input("Digite o novo email: ")
            atualizar_contato(contatos, indice, nome, telefone, email)

    elif escolha == "4":
        ver_contatos(contatos)
        indice_contato = input(
            "Digite o número do contato que deseja marcar como favorito: "
        )
        alternar_contato_favorito(contatos, indice_contato)
    elif escolha == "5":
        ver_contatos_favoritos(contatos)
    elif escolha == "6":
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja deletar: ")
        deletar_contato(contatos, indice_contato)
        ver_contatos(contatos)
    elif escolha == "7":
        break

    else:
        print("Opção inválida. Escolha um número de 1 a 7.")

print("Programa finalizado")
