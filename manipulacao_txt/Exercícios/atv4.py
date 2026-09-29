def criar_arquivo():
    with open("nomes.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Carlos\n")
        arquivo.write("Natalia\n")
        arquivo.write("Lorena\n")
        arquivo.write("Mariana\n")
        arquivo.write("Yasminn\n")
        arquivo.write("Yasmin\n")
        arquivo.write("Nicolas\n")


def contar_linhas():
    quantidade = 0

    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            quantidade += 1

    print(f"O arquivo possui {quantidade} linhas.")


criar_arquivo()
contar_linhas()