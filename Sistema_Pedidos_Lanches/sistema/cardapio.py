from tabulate import tabulate 

cardapio = []

def adicionar_item(cardapio):
    id = int(input("Digite o ID do item: "))
    nome = input("Digite o nome do item: ")
    preco = float(input("Digite o preço por unidade: "))
    
    item = {
        "ID": id,
        "Nome": nome,
        "Preço": preco
    }
    
    cardapio.append(item)
    
def exibir_cardapio(cardapio):
    tabela = [[item["ID"], item["Nome"], item["Preço"]] for item in cardapio]
    print(tabulate(tabela, headers=["Id", "Nome", "Preço"], tablefmt="fancy_grid"))
    
def burcar_item(cardapio):
    op = input("1 - Procurar por nome\n 2 - Procurar por ID")

    if op == 1:
        n = input("Digite o nome do item: ").strip().lower()
        for i in cardapio: 
            if i["Nome"] == n:
                return i
                
    if op == 2: 
        id = int(input("Digite o ID do item: "))
        for i in cardapio: 
            if i["ID"] == id:
                return i
    
    if op not in [1, 2]:
        return None