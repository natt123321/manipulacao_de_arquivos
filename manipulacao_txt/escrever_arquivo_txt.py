# modo "r" -  abre o arquivo para leitura
# modo "w" abre para escrita e apaga o conteudo existente
# modo"a" adiciona novo conteudo no final do arquivo
# modo "x" cria um arquivo novo e gera erro se ele ja existir

def criar_arquivo():
    # O "with" fecha o arquivo automaticamente
    # o "open()" é uma função para leitura ou escrita de arquivos
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Yasminn\n")
        arquivo.write("Yasmin\n")
        arquivo.write("Mariana\n")


criar_arquivo()

def adicionar_aluno(nome):
     with open("alunos.txt", "a", encoding="utf-8") as arquivo:
         arquivo.write(nome + "\n")

adicionar_aluno("Natalia")
adicionar_aluno("Carlos")
adicionar_aluno("Lorena")

def listar_alunos():
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print(f" O conteúdo do arquivo 'alunos' é: {conteudo}")

listar_alunos()

def listar_alunos_individual():
    lista_alunos = []
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            lista_alunos.append(linha.strip())

    print(f"Lista de alunos: {lista_alunos}")

listar_alunos_individual()

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))

    with open("cadastro.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}; {idade}\n")

    print(f"Aluno cadastrado com sucesso!")

cadastrar_aluno()

def listar_cadastro():
    itens_cadastro = []
    with open("cadastro.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(";")

            objeto = {
                "nome": nome,
                "idade": idade
            }

            itens_cadastro.append(objeto)
            print(f"Itens cadastrados: {itens_cadastro}")

listar_cadastro()