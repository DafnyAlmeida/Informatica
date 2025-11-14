from tabulate import tabulate
def carregar_cardapio(cardapio):
    id = int(input("Digite o id do cardapio: "))
    nome = input("Digite o nome do item: ")
    preco = float(input("Digite o preço do item: "))
    
    item = {
        "Id": id, 
        "Nome": nome, 
        "Preço": preco
    }
    
    cardapio.append(item)
    print("Item adicionado com sucesso!")

def exibir_cardapio(cardapio):
    tabela = [[item["Id"], item["Nome"], item["Preço"]] for item in cardapio]
    print(tabulate(tabela, headers=["Id", "Nome", "Preço"], tablefmt="fancy_grid"))
    
def adicionar_pedido(cardapio, pedidos):
    pedido_nome = input("Digite o nome da pedido: ").strip().lower()
    for i in cardapio:
        if pedido_nome in i["Nome"]:
            quantida = int(input("Digite a quantidade: "))
            id = i["Id"]
            preco = i["Preço"] * quantida
        else:
            print("O item não esta no cardapio")
        
    pedido = {
        "Nome": pedido_nome,
        "Id": id,
        "Quant": quantida,
        "Preço": preco
    }
    
    pedidos.append(pedido)
    print("Pedido adicionado com sucesso!")
    
def exibir_pedido(pedidos):
    for i in pedidos:
        total += i["Preço"]
    tabela = [[item["Id"], item["Nome"], item["Preço"]] for item in pedidos]
    print(tabulate(tabela, headers=["Id", "Nome", "Preço", "Total"], tablefmt="fancy_grid"))
    print("total")
    
def remover_item(pedidos):
    id_remover = int(input("Digite o id do item que deseja remover: "))
    for i in pedidos:
        if id_remover == i["Id"]:
            pedidos.remove(i)
    print("Item removido com sucesso!")

