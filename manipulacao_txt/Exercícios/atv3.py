def criar_arquivo():
    with open("frases.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Primeira frase.\n")


def adicionar_frase():
    frase = input("Digite uma frase: ")

    with open("frases.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(frase + "\n")


criar_arquivo()

adicionar_frase()
adicionar_frase()