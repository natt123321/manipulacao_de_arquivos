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
        # coloca esse registro dentro da "caixa"


# listar todos os pokemons que um treinador tem

nome_treinador = input("Digite o nome do treinador: ")
treinador_encontrado = False

for treinador in treinadores:
    if treinador["nome"] == nome_treinador:
        treinador_encontrado = True

        pokemons_treinador = []

        for pokemon in pokemons:
            if pokemon["treinador"] == treinador["nome"]:
                pokemons_treinador.append(pokemon)

        if len(pokemons_treinador) == 0:
            print("Esse treinador não possui nenhum Pokémon.")
        else:
            print("\nPokémon do treinador:")

            for pokemon in pokemons_treinador:
                print("Nome:", pokemon["nome"])
                print("Tipo:", pokemon["tipo"])
                print("Nível:", pokemon["nivel"])
                print()

if treinador_encontrado == False:
    print("Treinador não encontrado :/")


# contar quantos pokemons um treinador tem

nome_treinador = input("Digite o nome do treinador: ")
contador = 0

for pokemon in pokemons:
    if nome_treinador == pokemon["treinador"]:
        contador += 1

print("Quantidade de pokémon:", contador)


# ver o pokemon com maior nivel de um treinador

nome_treinador = input("Digite o nome do treinador: ")
maior_nivel = 0
pokemon_maior_nivel = None

for pokemon in pokemons:
    if nome_treinador == pokemon["treinador"]:
        if int(pokemon["nivel"]) > maior_nivel:
            maior_nivel = int(pokemon["nivel"])
            pokemon_maior_nivel = pokemon

if pokemon_maior_nivel == None:
    print("Treinador não encontrado ou não possui Pokémon.")
else:
    print("Nome:", pokemon_maior_nivel["nome"])
    print("Nível:", pokemon_maior_nivel["nivel"])
    print("Tipo:", pokemon_maior_nivel["tipo"])


# ver o pokemon com menor nivel de um treinador

nome_treinador = input("Digite o nome do treinador: ")
menor_nivel = 101
pokemon_menor_nivel = None

for pokemon in pokemons:
    if nome_treinador == pokemon["treinador"]:
        if int(pokemon["nivel"]) < menor_nivel:
            menor_nivel = int(pokemon["nivel"])
            pokemon_menor_nivel = pokemon

if pokemon_menor_nivel == None:
    print("Treinador não encontrado ou não possui Pokémon.")
else:
    print("Nome:", pokemon_menor_nivel["nome"])
    print("Nível:", pokemon_menor_nivel["nivel"])
    print("Tipo:", pokemon_menor_nivel["tipo"])


# Buscar pokemon por tipagem

tipo_busca = input("Digite o tipo: ")
pokemon_encontrado = False

for pokemon in pokemons:
    if tipo_busca == pokemon["tipo"]:
        print("Nome:", pokemon["nome"])
        print("Nível:", pokemon["nivel"])
        pokemon_encontrado = True

if pokemon_encontrado == False:
    print("Nenhum Pokémon desse tipo foi encontrado.")