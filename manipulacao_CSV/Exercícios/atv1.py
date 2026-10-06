import csv

treinadores = []

with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for treinador in leitor:
        treinadores.append(treinador)
        #coloca esse registro dentro da "caixa"

while True:
    print("===== TREINADORES POKÉMON =====")
    print("1 - Listar todos os treinadores")
    print("2 - Buscar treinador pelo nome")
    print("3 - Listar treinadores de uma região")
    print("4 - Mostrar treinador com maior nível")
    print("5 - Mostrar treinador com menor nível")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        for treinador in treinadores:
            print("Nome:", treinador["nome"])
            print("Região:", treinador["regiao"])
            print("Nível:", treinador["nivel"])

    elif opcao == "2":
        nome_busca = input("Digite o nome do treinador: ")
        nome_encontrado = False

        for treinador in treinadores:
            if nome_busca in treinador["nome"]:
                print("Nome:", treinador["nome"])
                print("Região:", treinador["regiao"])
                print("Nível:", treinador["nivel"])
                nome_encontrado = True

        if nome_encontrado == False:
            print("Treinador não encontrado :/")

    elif opcao == "3":
        regiao_busca = input("Digite a região: ")
        regiao_encontrada = False

        for treinador in treinadores:
            if regiao_busca == treinador["regiao"]:
                print("Nome:", treinador["nome"])
                regiao_encontrada = True

        if regiao_encontrada == False:
            print("Região não encontrada :/")

    elif opcao == "4":
        maior_nivel = 0
        treinador_maior_nivel = None

        for treinador in treinadores:
            if int(treinador["nivel"]) > maior_nivel:
                maior_nivel = int(treinador["nivel"])
                treinador_maior_nivel = treinador
        print("Nome:", treinador_maior_nivel["nome"])
        print("Nível:", treinador_maior_nivel["nivel"])
        print("Região:", treinador_maior_nivel["regiao"])

    elif opcao == "5":
        menor_nivel = 101
        treinador_menor_nivel = None

        for treinador in treinadores:
            if int(treinador["nivel"]) < menor_nivel:
                menor_nivel = int(treinador["nivel"])
                treinador_menor_nivel = treinador
        print("Nome:", treinador_menor_nivel["nome"])
        print("Nível:", treinador_menor_nivel["nivel"])
        print("Região:", treinador_menor_nivel["regiao"])


    elif opcao == "6":
        break