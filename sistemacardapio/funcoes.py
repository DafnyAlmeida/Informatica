from tabulate import tabulate


def exibir_cardapio(cardapio):
    if not cardapio:
        print("Cardapio não estabelecido")
    else:
        tabela = [[item["Id"], item["Nome"], item["Preço"]] for item in cardapio]
        print(tabulate(tabela, headers=["Id", "Nome", "Preço"], tablefmt="fancy_grid"))
    
def adicionar_pedido(cardapio, pedidos):
    pedido_nome = input("Digite o nome da pedido: ").strip().lower()
    encontrado = False
    for i in cardapio:
        if pedido_nome in i["Nome"].strip().lower():
            quantida = int(input("Digite a quantidade: "))
            preco = i["Preço"] * quantida
            pedido = {
                "Nome": i["Nome"],
                "Id": i["Id"],
                "Quant": quantida,
                "Preço": preco
            }
            pedidos.append(pedido)
            print("Pedido adicionado com sucesso!")
            encontrado = True
            break
        if not encontrado:
            print("O item não esta no cardapio")
    
def exibir_pedido(pedidos):
    total = sum(item["Preço"] for item in pedidos)
    tabela = [[item["Id"], item["Nome"], item["Preço"]] for item in pedidos]
    tabela.append(["", "Total", total])
    print(tabulate(tabela, headers=["Id", "Nome", "Preço"], tablefmt="fancy_grid"))
    
def remover_item(pedidos):
    tipo = (input("Deseja remover tudo ou por quantidade: (tudo/quantidade)")).lower().strip()
    
    match tipo:
        case "tudo":
            nome_remover = input("Digite o item que deseja remover: ").lower().strip()
            for i in pedidos:
                if nome_remover == i["Nome"]:
                    pedidos.remove(i)
            print("Item removido com sucesso!")
            
        case "quantidade":
            nome_remover = input("Digite o item que deseja remover: ").lower().strip()
            quant_remover = int(input("Digite a quantidade certa: "))
            for i in pedidos:
                if nome_remover == i["Nome"]:
                    i["Quant"] = quant_remover
                    print("Quantidade ajustada com sucesso!")
            
        case _:
            print("Valor inválido, tente novamente")
    

