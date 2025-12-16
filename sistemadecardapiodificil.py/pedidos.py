from cardapio import buscar_item

def novo_pedido(cardapio):
    pedido = {
        "id": None,
        "itens": [],
        "total": 0
    }

    while True:
        id_item = int(input("Digite o ID do item (0 para finalizar): "))
        if id_item == 0:
            break

        quantidade = int(input("Digite a quantidade: "))

        item = buscar_item(cardapio, id_item)
        if item is None:
            print("Item não encontrado!")
        else:
            pedido["itens"].append({
                "id": id_item,
                "quantidade": quantidade
            })

    return pedido


def calcular_total(pedido, cardapio):
    total = 0
    total_itens = 0

    for i in pedido["itens"]:
        item = buscar_item(cardapio, i["id"])
        total += item["preco"] * i["quantidade"]
        total_itens += i["quantidade"]

    if total > 50:
        total = total * 0.9  # desconto de 10%
        print("Desconto de 10% aplicado!")

    if total_itens > 5:
        print("Você ganhou um brinde!")

    pedido["total"] = total


def exibir_pedido(pedido, cardapio):
    print("\nPEDIDO")
    for i in pedido["itens"]:
        item = buscar_item(cardapio, i["id"])
        print(f"{item['nome']} - Quantidade: {i['quantidade']}")

    print(f"Total: R$ {pedido['total']}")
