def criar_arquivo():
    with open("vendas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;Notebook;3500.00\n")
        arquivo.write("Bruno;Mouse;80.00\n")
        arquivo.write("Carlos;Teclado;150.00\n")
        arquivo.write("Ana;Monitor;900.00\n")
        arquivo.write("Daniela;Notebook;3500.00\n")
        arquivo.write("Bruno;Headset;200.00\n")
        arquivo.write("Carlos;Mouse;80.00\n")
        arquivo.write("Ana;Teclado;150.00\n")
        arquivo.write("Daniela;Monitor;900.00\n")


def gerar_relatorio():
    vendas = []
    total_vendas = 0

    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            venda = {
                "vendedor": dados[0],
                "produto": dados[1],
                "valor": float(dados[2])
            }

            vendas.append(venda)

    print("VENDAS:")

    for venda in vendas:
        print(
            f"{venda['vendedor']} - "
            f"{venda['produto']} - "
            f"R$ {venda['valor']:.2f}"
        )

        total_vendas += venda["valor"]

    print(f"\nTOTAL DE VENDAS: R$ {total_vendas:.2f}")

    vendedores = {}

    for venda in vendas:
        vendedor = venda["vendedor"]

        if vendedor in vendedores:
            vendedores[vendedor] += 1
        else:
            vendedores[vendedor] = 1

    print("\nQuantidade de vendas:")

    for vendedor in vendedores:
        print(f"{vendedor}: {vendedores[vendedor]}")


criar_arquivo()
gerar_relatorio()