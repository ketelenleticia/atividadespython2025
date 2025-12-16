from turmas import *
from alunos import *
from relacoes import *

turmas = []
alunos = []
relacoes = []

while True:
    print("\nMENU")
    print("1 - Criar turma")
    print("2 - Cadastrar aluno")
    print("3 - Adicionar aluno à turma")
    print("4 - Listar turmas")
    print("5 - Listar alunos")
    print("6 - Listar alunos de uma turma")
    print("7 - Remover aluno da turma")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criar_turma(turmas)

    elif opcao == "2":
        cadastrar_aluno(alunos)

    elif opcao == "3":
        adicionar_aluno_na_turma(turmas, alunos, relacoes)

    elif opcao == "4":
        listar_turmas(turmas)

    elif opcao == "5":
        listar_alunos(alunos)

    elif opcao == "6":
        listar_alunos_da_turma(relacoes, alunos, turmas)

    elif opcao == "7":
        remover_aluno_da_turma(relacoes)

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")