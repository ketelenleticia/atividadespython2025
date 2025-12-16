from cardapio import *
from pedidos import *
from relatorios import *

cardapio = carregar_cardapio()
pedidos = []
contador_pedidos = 1

while True:
    print("\nMENU")
    print("1 - Exibir cardápio")
    print("2 - Fazer novo pedido")
    print("3 - Listar pedidos")
    print("4 - Buscar pedido por ID")
    print("5 - Relatório financeiro")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exibir_cardapio(cardapio)

    elif opcao == "2":
        pedido = novo_pedido(cardapio)
        pedido["id"] = contador_pedidos
        calcular_total(pedido, cardapio)
        pedidos.append(pedido)
        contador_pedidos += 1
        exibir_pedido(pedido, cardapio)

    elif opcao == "3":
        listar_pedidos(pedidos, cardapio)

    elif opcao == "4":
        id_pedido = int(input("Digite o ID do pedido: "))
        pedido = buscar_pedido_por_id(pedidos, id_pedido)
        if pedido:
            exibir_pedido(pedido, cardapio)
        else:
            print("Pedido não encontrado.")

    elif opcao == "5":
        rel = relatorio_financeiro(pedidos)
        print("Total vendido:", rel["total_vendido"])
        print("Pedido mais caro:", rel["pedido_mais_caro"])
        print("Quantidade de itens vendidos:", rel["qtd_itens"])

    elif opcao == "6":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
