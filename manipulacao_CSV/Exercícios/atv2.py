import csv

pokemons = []

with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for pokemon in leitor:
        pokemons.append(pokemon)
        #coloca esse registro dentro da "caixa"

nome_treinador = input("Digite o nome do treinador: ")
treinador_encontrado = False

#listar todos os pokemons que um treinador tem
for pokemon in pokemons:
    if pokemon["treinador"] == nome_treinador:
        print("Nome do pokémon:", pokemon["nome"])
        print("Tipo:", pokemon["tipo"])
        print("Nível:", pokemon["nivel"])
        treinador_encontrado = True

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

print("Nome:", pokemon_menor_nivel["nome"])
print("Nível:", pokemon_menor_nivel["nivel"])
print("Tipo:", pokemon_menor_nivel["tipo"])

# Buscar pokemon por tipagem
tipo_busca = input("Digite o tipo: ")

for pokemon in pokemons:
    if tipo_busca == pokemon["tipo"]:
        print("Nome:", pokemon["nome"])
        print("Nível:", pokemon["nivel"])





