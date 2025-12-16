from alunos import buscar_aluno_por_id
from turmas import buscar_turma_por_id
from tabulate import tabulate

def adicionar_aluno_na_turma(turmas, alunos, relacoes):
    id_aluno = int(input("Digite o ID do aluno: "))
    id_turma = int(input("Digite o ID da turma: "))

    aluno = buscar_aluno_por_id(alunos, id_aluno)
    turma = buscar_turma_por_id(turmas, id_turma)

    if aluno is None or turma is None:
        print("Aluno ou turma não encontrado!")
        return

    relacoes.append({
        "id_aluno": id_aluno,
        "id_turma": id_turma
    })

    print("Aluno adicionado à turma com sucesso!")

def listar_alunos_da_turma(relacoes, alunos, turmas):
    id_turma = int(input("Digite o ID da turma: "))
    turma = buscar_turma_por_id(turmas, id_turma)

    if turma is None:
        print("Turma não encontrada!")
        return

    tabela = []

    for r in relacoes:
        if r["id_turma"] == id_turma:
            aluno = buscar_aluno_por_id(alunos, r["id_aluno"])
            tabela.append([aluno["id"], aluno["nome"]])

    if len(tabela) == 0:
        print("Nenhum aluno nessa turma.")
    else:
        print(f"Alunos da turma {turma['nome']}:")
        print(tabulate(tabela, headers=["ID", "Aluno"], tablefmt="fancy_grid"))

def remover_aluno_da_turma(relacoes):
    id_aluno = int(input("Digite o ID do aluno: "))
    id_turma = int(input("Digite o ID da turma: "))

    for r in relacoes:
        if r["id_aluno"] == id_aluno and r["id_turma"] == id_turma:
            relacoes.remove(r)
            print("Aluno removido da turma!")
            return

    print("Relação não encontrada!")
