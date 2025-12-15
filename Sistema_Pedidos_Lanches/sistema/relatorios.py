from tabulate import tabulate

def listar_pedidos(pedidos):
    tabela = []
    for i in pedidos:
        tabela.append([
            i["ID_pedido"],
            len(i["Itens"]),
            f"R$ {i['Total']}"
        ])
     
    print(tabulate(tabela, headers=["ID Pedido", "Qtd Itens", "Total"], tablefmt="grid"))

def buscar_pedido_por_id(pedidos):
    id_pedido = int(input("Digite o ID do item que deseja buscar: "))
    for i in pedidos:
        if i["ID_pedido"] == id_pedido:
            print(f"O pedido foi {i}")

def relatorio_financeiro(pedidos):
    ganho = 0
    quan_total = 0
    mais_caro = pedidos[0]
    for pedido in pedidos:
        ganho += pedido["Total"]
        if pedido["Total"] > mais_caro["Total"]:
            mais_caro = pedido
    for i in pedido["Itens"]:
        quan_total += i["Quantidade"]
        
        