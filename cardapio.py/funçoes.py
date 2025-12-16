from tabulate import tabulate
pedido=[]
def carrega_cardapio():
    cardapio=[
        {"id": 1,"nome":"hambúrger","preço":12.5},
        {"id": 2,"nome":"pizza","preço":30},
        {"id": 3,"nome":"refrigerante","preço":5}
    ]
    return cardapio
def exibir_cardapio(cardapio):
    print("=====cardapio=====")
    tabela=[]
    for item in cardapio:
        tabela.append([item["id"],item["nome"],item["preço"]])
    print(tabulate(tabela,headers=["ID","nome","preço"],tablefmt="fancy-grind")) 
    return   

def adicionar_pedido(cardapio, pedido):
    id=int(input("digite ID do item: "))
    qtd=int(input("digite a quantidade: "))
    item=cardapio[id]

    for item in cardapio:
        if item["id"]==id:
            total=item["preço"] * qtd 

        pedido.append({
            "item":item["nome"],
            "qtd": qtd,
            "total": total
        })
    print("Seu pedido foi adicionado!")

    print("ID nao foi encontrado")
    return   

def exibir_pedido(pedido):
    if not pedido:
        print("nao a pedidos")
        return
    print("====PEDIDOS====")
    tabela2=[]
    for item in pedido:
        tabela2.append([item["item"],item["qtd"],item["total"],])
    print(tabulate(tabela2,headers=["item","quantidade","total"],tablefmt="fancy-grind")) 
     
    total_geral=sum([item["total"] for item in pedido])
    print(f"o total da compra foi {total_geral}")  
    return   

def remover_item(pedido):
    if not pedido:
        print(" nao a nada para remover!")    
        return
    
    nome=input("digite um o nome do item para remover: ")

    for item in pedido:
        if item["item"].lower()==nome:
            pedido.remove(item)
            print(f"item {nome} foi removido")
    

    print("item nao encontrado")
    return  
         
         

