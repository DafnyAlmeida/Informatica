from random import randint
from tabulate import tabulate 

def novo_pedido(cardapio, pedidos):
    id_pedido = randint(1, 10000)
    
    pedido = {
        "ID_pedido": id_pedido,
        "Itens": [],
        "Total": 0
    }
    
    adi = "s"
    
    while adi == "s":
        adi = input("Deseja adicionar item ao pedido s/n? ")
        
        if adi != "s":
            print("Programa encerrado!")
            break
        
        op = int(input("\n 1 - Adicionar item ao pedido por ID \n 2 - Adicionar item ao pedido por nome: "))
        
        id_item = None
        nome = None
        preco = 0
        
        if op == 1: 
            id = int(input("Digite o ID: "))
            for i in cardapio:
                if i["ID"] == id:
                    id_item = i["ID"]
                    nome = i["Nome"]
            quant = int(input("Digite a quantidade: "))
        
        if op == 2: 
            nome = input("Digite o nome: ")
            for i in cardapio:
                if i["Nome"] == nome:
                    id_item = i["ID"]
                    nome = i["Nome"]
                    preco = i["Preço"]
        
        quant = int(input("Digite a quantidade: "))
        
        item = {
            "ID": id_item,
            "Quantidade": quant,
            "Nome": nome,
            "Preço": preco
        }
        
        pedido["Itens"].append(item)
        
        pedido["Total"] = calcular_total(pedido)
        
    pedidos.append(pedido)
            
def calcular_total(pedido):
    total = 0
    for item in pedido["Itens"]:
        total = item["Preço"] * item["Quantidade"]
        
    if total > 50:
        total *= 0.9
    
    return total

def exibir_pedido(pedido):
    tabela = [[item["ID"], item["Quantidade"], item["Nome"], item["Preço"]] for item in pedido["Itens"]]
    print(tabulate(tabela, headers=["Id", "Quantidade", "Nome", "Preço"], tablefmt="fancy_grid"))
    print(f"O total foi de {pedido["Total"]}")