def criar_arquivo():
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;8.5\n")
        arquivo.write("Bruno;5.0\n")
        arquivo.write("Carlos;7.2\n")
        arquivo.write("Daniela;9.0\n")
        arquivo.write("Eduardo;4.5\n")
        arquivo.write("Fernanda;6.8\n")
        arquivo.write("Gabriel;5.9\n")


def listar_aprovados():
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            nome = dados[0]
            nota = float(dados[1])

            if nota >= 6:
                print(f"{nome} - {nota}")


criar_arquivo()
listar_aprovados()