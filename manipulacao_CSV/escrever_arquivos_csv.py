import csv
from doctest import debug_script


def criar_csv():
    with open("alunos.csv", "w", newline="",encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "Curso"])

        escritor.writerow(["Natalia", 16, "DEV"])
        escritor.writerow(["Carlos", 16, "Eletromecânica"])
        escritor.writerow(["Yasminn", 16, "Eletroeletrônica"])

#criar_csv()

def salvar_alunos():
    alunos = [
        ["Natalia", 16, "DEV"],
        ["Carlos", 16, "DEV"],
        ["Yasminn", 16, "DEV"]
        ]

    with open("novos_alunos.csv", "w", newline="",encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "Curso"])

        escritor.writerows(alunos)

#salvar_alunos()

def ler_csv():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor)

        for linha in leitor:
            print(linha[0])

#ler_csv()

def exibir_alunos():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        alunos = csv.DictReader(arquivo)

        for aluno in alunos:
            print(aluno)

#exibir_alunos()

def cadastrar_aluno():
    # o 0 é o inicio do arquivo e o 2 é o final, ele move o cursor para o inicio do arquivo.
    with open("novos_alunos.csv", "a+", newline="", encoding="utf-8") as arquivo:
        arquivo.seek(0,2)
        nome = input("Digite o nome do(a) aluno(a): ")
        idade = int(input("Digite a idade do(a) aluno(a): "))
        curso = input("Digite o curso do(a) aluno(a): ")

        escritor = csv.writer(arquivo)

        escritor.writerow([nome, idade, curso])

cadastrar_aluno()

def deletar_aluno():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        alunos = list(leitor)

        with open("novos_alunos.csv", "w",newline="", encoding="utf-8") as arquivo:
            cabecalho = ["Nome", "Idade", "Curso"]
            escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)

            escritor.writeheader()

            aluno_apagar = input("Digite o nome do aluno(a) que deseja apagar: ")

            for aluno in alunos:
                if alunos["Nome"] != aluno_apagar:
                    escritor.writerow(aluno)

deletar_aluno()
