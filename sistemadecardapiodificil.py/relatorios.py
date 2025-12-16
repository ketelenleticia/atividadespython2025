def listar_pedidos(pedidos, cardapio):
    if len(pedidos) == 0:
        print("Nenhum pedido registrado.")
        return

    for p in pedidos:
        print(f"Pedido {p['id']} - Total: R$ {p['total']}")


def buscar_pedido_por_id(pedidos, id_pedido):
    for p in pedidos:
        if p["id"] == id_pedido:
            return p
    return None


def relatorio_financeiro(pedidos):
    total_vendido = 0
    pedido_mais_caro = None
    qtd_itens = 0

    for p in pedidos:
        total_vendido += p["total"]

        if pedido_mais_caro is None or p["total"] > pedido_mais_caro["total"]:
            pedido_mais_caro = p

        for i in p["itens"]:
            qtd_itens += i["quantidade"]

    return {
        "total_vendido": total_vendido,
        "pedido_mais_caro": pedido_mais_caro,
        "qtd_itens": qtd_itens
    }
