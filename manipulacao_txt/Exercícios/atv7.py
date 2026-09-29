def criar_arquivo():
    with open("nomes.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Carlos\n")
        arquivo.write("Natalia\n")
        arquivo.write("Lorena\n")
        arquivo.write("Mariana\n")
        arquivo.write("Yasmin\n")
        arquivo.write("Yasminn\n")
        arquivo.write("Nicolas\n")


def buscar_nome():
    nomes = []

    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nomes.append(linha.strip())

    nome_pesquisar = input("Digite o nome que deseja pesquisar: ")

    if nome_pesquisar in nomes:
        print("Nome encontrado!")
    else:
        print("Nome não encontrado!")


criar_arquivo()
buscar_nome()