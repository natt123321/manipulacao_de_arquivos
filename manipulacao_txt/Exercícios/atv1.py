def criar_arquivo():
    with open("mensagem.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Olá, mundo!\n")
        arquivo.write("Estou aprendendo Python.\n")
        arquivo.write("Estou estudando manipulação de arquivos.")


criar_arquivo()

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

criar_arquivo()
ler_arquivo("mensagem.txt")
