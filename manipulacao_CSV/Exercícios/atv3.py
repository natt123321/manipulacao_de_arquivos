import csv

treinadores = []

with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for treinador in leitor:
        treinadores.append(treinador)

pokemons = []

with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for pokemon in leitor:
        pokemons.append(pokemon)


# Preparando os dados por treinador

soma_niveis = {}
quantidade_pokemons = {}

for pokemon in pokemons:
    treinador = pokemon["treinador"]

    if treinador not in soma_niveis:
        soma_niveis[treinador] = 0
        quantidade_pokemons[treinador] = 0

    quantidade_pokemons[treinador] += 1
    soma_niveis[treinador] += int(pokemon["nivel"])


# Preparando os dados por tipo

soma_niveis_tipo = {}
quantidade_pokemons_tipo = {}

for pokemon in pokemons:
    tipo = pokemon["tipo"]

    if tipo not in soma_niveis_tipo:
        soma_niveis_tipo[tipo] = 0
        quantidade_pokemons_tipo[tipo] = 0

    quantidade_pokemons_tipo[tipo] += 1
    soma_niveis_tipo[tipo] += int(pokemon["nivel"])


while True:
    print("\n===== RELATÓRIOS =====")
    print("1 - Relatório de um treinador")
    print("2 - Média de nível dos Pokémon de um treinador")
    print("3 - Média de nível dos Pokémon por tipo")
    print("4 - Quantidade de Pokémon por treinador")
    print("5 - Quantidade de Pokémon por tipo")
    print("6 - Treinadores com nível acima de um valor")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")


    # Opção 1: Relatório de um treinador

    if opcao == "1":
        print("\n--- Relatório de um treinador ---")

        nome_treinador = input("Digite o nome do treinador: ")
        treinador_encontrado = False

        for treinador in treinadores:
            if nome_treinador == treinador["nome"]:
                print("Treinador:", treinador["nome"])
                print("Região:", treinador["regiao"])
                print("Nível do treinador:", treinador["nivel"])
                print("\nPokémon:")

                treinador_encontrado = True

                pokemon_encontrado = False

                for pokemon in pokemons:
                    if pokemon["treinador"] == nome_treinador:
                        print("-", pokemon["nome"], "-", pokemon["tipo"],
                              "- Nível", pokemon["nivel"])
                        pokemon_encontrado = True

                if pokemon_encontrado == False:
                    print("Esse treinador não possui nenhum Pokémon.")

        if treinador_encontrado == False:
            print("Treinador não encontrado :/")


    # Opção 2: Média de nível dos Pokémon de um treinador

    elif opcao == "2":
        print("\n--- Média de nível dos Pokémon de um treinador ---")

        nome_treinador = input("Digite o nome do treinador: ")

        if nome_treinador in soma_niveis:
            media = soma_niveis[nome_treinador] / quantidade_pokemons[nome_treinador]

            print("Treinador:", nome_treinador)
            print("Média dos pokémons:", media)

        else:
            print("Treinador não encontrado :/")


    # Opção 3: Média de nível dos Pokémon por tipo

    elif opcao == "3":
        print("\n--- Média de nível dos Pokémon por tipo ---")

        tipo_busca = input("Digite o tipo: ")

        if tipo_busca in soma_niveis_tipo:
            media = soma_niveis_tipo[tipo_busca] / quantidade_pokemons_tipo[tipo_busca]

            print("Tipo:", tipo_busca)
            print("Média dos pokémons:", media)

        else:
            print("Tipo não encontrado :/")


    # Opção 4: Quantidade de Pokémon por treinador

    elif opcao == "4":
        print("\n--- Quantidade de Pokémon por treinador ---")

        for treinador in quantidade_pokemons:
            print("Treinador:", treinador)
            print("Quantidade de pokémon:", quantidade_pokemons[treinador])


    # Opção 5: Quantidade de Pokémon por tipo

    elif opcao == "5":
        print("\n--- Quantidade de Pokémon por tipo ---")

        for tipo in quantidade_pokemons_tipo:
            print("Tipo:", tipo)
            print("Quantidade de pokémon:", quantidade_pokemons_tipo[tipo])


    # Opção 6: Treinadores com nível acima de um valor

    elif opcao == "6":
        print("\n--- Treinadores com nível acima de um valor ---")

        nivel_minimo = int(input("Digite o nível mínimo: "))

        for treinador in treinadores:
            if int(treinador["nivel"]) > nivel_minimo:
                print("Treinador:", treinador["nome"])
                print("Nível:", int(treinador["nivel"]))


    # Opção 7: Sair

    elif opcao == "7":
        print("Saindo...")
        break

    else:
        print("Opção inválida :/")