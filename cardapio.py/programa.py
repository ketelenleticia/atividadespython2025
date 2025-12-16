from funçoes import *
def menu():
    cardapio=carrega_cardapio()
    pedido=[]
    while True:
        print("Cardápio")
        print(" 1 - ver cardapio")
        print(" 2 - Adiconar item ao pedido")
        print(" 3 - ver pedido")
        print(" 4 - Remover item")
        print(" 0- Finalizar")

        opçao=input("Escolha uma opçao: ")

        if opçao =="1":
            exibir_cardapio(cardapio)
        elif  opçao=="2":
             adicionar_pedido(cardapio,pedido)
        elif opçao=="3" :
             exibir_pedido(pedido)
        elif opçao=="4" :
             remover_item(pedido)
        elif opçao=="0":
            print("fim")
            break

menu()        