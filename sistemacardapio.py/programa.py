from funcoes import *
cardapio = criar_cardapio()
pedido = []

while True:
    print("\nMENU")
    print("1 - Ver cardápio")
    print("2 - Adicionar item ao pedido")
    print("3 - Ver pedido")
    print("4 - Remover item")
    print("0 - Finalizar")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exibir_cardapio(cardapio)

    elif opcao == "2":
        exibir_cardapio(cardapio)
        adicionar_pedido(cardapio, pedido)

    elif opcao == "3":
        exibir_pedido(pedido)

    elif opcao == "4":
        exibir_pedido(pedido)
        remover_item(pedido)

    elif opcao == "0":
        print("Pedido finalizado. Obrigado!")
        break