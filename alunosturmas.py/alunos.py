import random
from tabulate import tabulate

def cadastrar_aluno(alunos):
    nome = input("Digite o nome do aluno: ")

    aluno = {
        "id": random.randint(1, 1000),
        "nome": nome
    }

    alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

def listar_alunos(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    tabela = []
    for a in alunos:
        tabela.append([a["id"], a["nome"]])

    print(tabulate(tabela, headers=["ID", "Aluno"], tablefmt="fancy_grid"))

def buscar_aluno_por_id(alunos, id_busca):
    for a in alunos:
        if a["id"] == id_busca:
            return a
    return None
