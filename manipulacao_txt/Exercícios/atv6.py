def criar_arquivo():
    with open("nomes.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Carlos\n")
        arquivo.write("Natalia\n")
        arquivo.write("Lorena\n")
        arquivo.write("Mariana\n")
        arquivo.write("Yasmin\n")
        arquivo.write("Yasminn\n")
        arquivo.write("Nicolas\n")


def carregar_nomes():
    nomes = []

    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome = linha.strip()
            nomes.append(nome)

    print(nomes)


criar_arquivo()
carregar_nomes()