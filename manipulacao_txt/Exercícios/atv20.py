def criar_arquivo():
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("1;Ana Silva;17;Desenvolvimento de Sistemas\n")
        arquivo.write("2;Bruno Souza;18;Desenvolvimento de Sistemas\n")
        arquivo.write("3;Carlos Oliveira;17;Desenvolvimento de Sistemas\n")
        arquivo.write("4;Daniela Santos;18;Desenvolvimento de Sistemas\n")
        arquivo.write("5;Eduardo Lima;17;Desenvolvimento de Sistemas\n")


def salvar_alunos(alunos):
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        for aluno in alunos:
            arquivo.write(
                f"{aluno['id']};"
                f"{aluno['nome']};"
                f"{aluno['idade']};"
                f"{aluno['curso']}\n"
            )


def sistema_alunos():
    alunos = []

    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            aluno = {
                "id": int(dados[0]),
                "nome": dados[1],
                "idade": int(dados[2]),
                "curso": dados[3]
            }

            alunos.append(aluno)

    while True:
        print("\n===== SISTEMA DE ALUNOS =====")
        print("1 - Listar alunos")
        print("2 - Buscar aluno")
        print("3 - Cadastrar aluno")
        print("4 - Remover aluno")
        print("5 - Alterar aluno")
        print("6 - Sair")

        opcao = input("Escolha: ")

        # LISTAR
        if opcao == "1":

            for aluno in alunos:
                print(
                    f"{aluno['id']} - "
                    f"{aluno['nome']} - "
                    f"{aluno['idade']} anos"
                )

        # BUSCAR
        elif opcao == "2":

            id_pesquisa = int(input("Digite o ID: "))
            encontrado = False

            for aluno in alunos:
                if aluno["id"] == id_pesquisa:
                    print("Aluno encontrado:")
                    print(aluno["nome"])
                    print(f"{aluno['idade']} anos")
                    print(aluno["curso"])

                    encontrado = True

            if encontrado == False:
                print("Aluno não encontrado!")

        # CADASTRAR
        elif opcao == "3":

            id_novo = int(input("ID: "))
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            curso = input("Curso: ")

            aluno = {
                "id": id_novo,
                "nome": nome,
                "idade": idade,
                "curso": curso
            }

            alunos.append(aluno)
            salvar_alunos(alunos)

            print("Aluno cadastrado com sucesso!")

        # REMOVER
        elif opcao == "4":

            id_remover = int(input("Digite o ID do aluno: "))

            encontrado = False

            for aluno in alunos:
                if aluno["id"] == id_remover:
                    alunos.remove(aluno)
                    salvar_alunos(alunos)

                    print("Aluno removido!")
                    encontrado = True
                    break

            if encontrado == False:
                print("Aluno não encontrado!")

        # ALTERAR
        elif opcao == "5":

            id_alterar = int(input("Digite o ID do aluno: "))

            encontrado = False

            for aluno in alunos:
                if aluno["id"] == id_alterar:

                    aluno["nome"] = input("Novo nome: ")
                    aluno["idade"] = int(input("Nova idade: "))
                    aluno["curso"] = input("Novo curso: ")

                    salvar_alunos(alunos)

                    print("Aluno alterado!")
                    encontrado = True
                    break

            if encontrado == False:
                print("Aluno não encontrado!")

        # SAIR
        elif opcao == "6":
            print("Programa encerrado.")
            break

        # OPÇÃO INVÁLIDA
        else:
            print("Opção inválida!")


criar_arquivo()
sistema_alunos()