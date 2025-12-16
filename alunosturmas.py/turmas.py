om tabulate import tabulate

def criar_turma(turmas):
    nome = input("Digite o nome da turma: ")

    turma = {
        "id": random.randint(1, 1000),
        "nome": nome
    }

    turmas.append(turma)
    print("Turma criada com sucesso!")

def listar_turmas(turmas):
    if len(turmas) == 0:
        print("Nenhuma turma cadastrada.")
        return

    tabela = []
    for t in turmas:
        tabela.append([t["id"], t["nome"]])

    print(tabulate(tabela, headers=["ID", "Turma"], tablefmt="fancy_grid"))

def buscar_turma_por_id(turmas, id_busca):
    for t in turmas:
        if t["id"] == id_busca:
            return t
    return None
