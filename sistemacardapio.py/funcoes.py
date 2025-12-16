from tabulate import tabulate
def criar_cardapio():
    cardapio = [
        {"id": 1, "nome": "Hambúrguer", "preco": 12.5},
        {"id": 2, "nome": "Pizza", "preco": 30},
        {"id": 3, "nome": "Refrigerante", "preco": 5}
    ]
    return cardapio

def exibir_cardapio(cardapio):
    tabela = []

    for item in cardapio:
        tabela.append([item["id"], item["nome"], item["preco"]])

    print("\nCARDÁPIO")
    print(tabulate(
        tabela,
        headers=["ID", "Item", "Preço (R$)"],
        tablefmt="fancy_grid"
    ))


def adicionar_pedido(cardapio, pedido):
    id_item = int(input("Digite o ID do item: "))
    quantidade = int(input("Digite a quantidade: "))

    for item in cardapio:
        if item["id"] == id_item:
            total = item["preco"] * quantidade

            pedido.append({
                "item": item["nome"],
                "qtd": quantidade,
                "total": total
            })

            print("Item adicionado ao pedido!")
            return

    print("Item não encontrado!")

def exibir_pedido(pedido):
    if len(pedido) == 0:
        print("Pedido vazio!")
        return

    tabela = []
    total_geral = 0

    for item in pedido:
        tabela.append([item["item"], item["qtd"], item["total"]])
        total_geral += item["total"]

    print("\nSEU PEDIDO")
    print(tabulate(
        tabela,
        headers=["Item", "Quantidade", "Total (R$)"],
        tablefmt="fancy_grid"
    ))

    print(f"Total da compra: R$ {total_geral}")

def remover_item(pedido):
    nome = input("Digite o nome do item para remover: ")

    for item in pedido:
        if item["item"].lower() == nome.lower():
            pedido.remove(item)
            print("Item removido!")
            return

    print("Item não encontrado no pedido!")    
