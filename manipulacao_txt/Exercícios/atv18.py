def criar_arquivo():
    with open("produtos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Teclado;120.50;10\n")
        arquivo.write("Mouse;75.90;15\n")
        arquivo.write("Monitor;899.90;5\n")
        arquivo.write("Headset;150.00;8\n")
        arquivo.write("Webcam;210.00;4\n")


def calcular_estoque():
    produtos = []
    valor_total = 0

    with open("produtos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            produto = {
                "nome": dados[0],
                "preco": float(dados[1]),
                "quantidade": int(dados[2])
            }

            produtos.append(produto)

    for produto in produtos:
        valor = produto["preco"] * produto["quantidade"]
        valor_total += valor

    print(f"Valor total do estoque: R$ {valor_total:.2f}")


criar_arquivo()
calcular_estoque()