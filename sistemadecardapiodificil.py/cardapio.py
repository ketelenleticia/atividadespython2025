def carregar_cardapio():
    cardapio = [
        {"id": 1, "nome": "Hambúrguer", "preco": 12.50},
        {"id": 2, "nome": "Batata Frita", "preco": 7.00},
        {"id": 3, "nome": "Refrigerante", "preco": 5.00}
    ]
    return cardapio


def exibir_cardapio(cardapio):
    print("\nCARDÁPIO")
    for item in cardapio:
        print(f"{item['id']} - {item['nome']} - R$ {item['preco']}")


def buscar_item(cardapio, id_item):
    for item in cardapio:
        if item["id"] == id_item:
            return item
    return None
